# agentic-ai-cyberres
An AI agent that improves cyber resiliency by autonomously identifying enterprise applications and validating that the application's data is not corrupted.


# Pre-requisites
- Python (>= 3.12.6) runtime is needed to work with Bee Agent Framework.
- pip (>= 25.1.1) to manage packages for python
- LLM Inference provider: e.g. watsonx, Ollama, Groq, OpenAI, GCP, AWS Bedrock 

# Installation
1. Clone the repository

<pre><code>git clone https://github.com/IBM/agentic-ai-cyberres.git
# or if repo requires a ssh key instead of password
git clone git@github.com:IBM/agentic-ai-cyberres.git
</code></pre> 

2. Change into working directory
<pre><code>cd agentic-ai-cyberres
</code></pre> 

3. Setup virtual environment

<pre><code>python -m venv env_name
</code></pre>

4. Activate virtual environment

    <b>Windows</b>
    <pre><code>env_name\Scripts\activate
    </code></pre>

    <b>macOS/Linux</b>

    <pre><code>source env_name/bin/activate
    </code></pre>

5. Install dependencies
<pre><code>pip install -r requirements.txt
</code></pre>


   
# Using agentic-ai-cyberres agent

Currently there is only memory related examples integrted with BeeAI based Agentic AI framework. 
Added custom memory persistence with the langchain's SQL library
<pre><code># to run interactively
python src/chat_agent_unconstrained_memory.py
</code></pre>


