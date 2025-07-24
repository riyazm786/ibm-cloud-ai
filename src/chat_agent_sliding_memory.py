import asyncio
import sys
import traceback

from beeai_framework.agents import AgentExecutionConfig
from beeai_framework.agents.react import ReActAgent, ReActAgentRunOutput
from beeai_framework.backend import ChatModel
from beeai_framework.memory import SlidingMemory, SlidingMemoryConfig
from beeai_framework.backend import AssistantMessage
from beeai_framework.backend import UserMessage
from beeai_framework.tools.search.duckduckgo import DuckDuckGoSearchTool
from beeai_framework.tools.weather import OpenMeteoTool
from examples.helpers.io import ConsoleReader
from beeai_framework.errors import FrameworkError
from langchain_community.chat_message_histories import SQLChatMessageHistory



async def main() -> None:
    chat_model: ChatModel = ChatModel.from_name("ollama:granite3.3:8b")

    conv_history: SQLChatMessageHistory = get_conv_history()

    agent = ReActAgent(
        llm=chat_model, tools=[OpenMeteoTool(), DuckDuckGoSearchTool(max_results=3)], memory= await load_memory(conv_history)
    )

    reader = ConsoleReader()
    agent.memory

    reader.write("🛠️ System: ", "Agent initialized with DuckDuckGo and OpenMeteo tools.")

    for prompt in reader:
        output: ReActAgentRunOutput = await agent.run(
            prompt=prompt, execution=AgentExecutionConfig(total_max_retries=2, max_retries_per_step=3, max_iterations=8)
        ).on(
            "update",
            lambda data, event: handle_agent_update(data, conv_history, prompt, reader)
        )

def handle_agent_update(data, conv_history: SQLChatMessageHistory, user_message, reader):
    reader.write(f"Agent({data.update.key}) 🤖 : ", data.update.parsed_value)
    # update history
    if data.update.key == "final_answer":
        conv_history.add_user_message(user_message)
        conv_history.add_ai_message(data.update.parsed_value)

    
def get_conv_history():
    message_history = SQLChatMessageHistory(
        session_id='test_session', connection_string='sqlite:///my_chat_history.db'
    )
    
    return message_history

async def load_memory(conv_history: SQLChatMessageHistory ):
    memory = SlidingMemory(
        SlidingMemoryConfig(
            size=4,
            handlers={"removal_selector": lambda messages: messages[0]},  # Remove oldest message
        )
    )
    messages = conv_history.get_messages()
    for message in messages:
        if message.type == "human":
            await memory.add(UserMessage(content=message.content))
        if message.type == "ai":
            await memory.add(AssistantMessage(content=message.content))
    return memory

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except FrameworkError as e:
        traceback.print_exc()
        sys.exit(e.explain())
