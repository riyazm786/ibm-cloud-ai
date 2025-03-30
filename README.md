# agentic-ai-cyberres
An AI agent that improves cyber resiliency by autonomously identifying enterprise applications and validating that the application's data is not corrupted.


# Pre-requisites
1. Node.js (>= 18.0.0) runtime is needed to work with Bee Agent Framework.
2. LLM Inference provider
- e.g. watsonx, Ollama, Groq, OpenAI, GCP, AWS Bedrock 

# Installation
1. Clone the repository

<pre><code>  git clone https://github.ibm.com/efarr/agentic-ai-cyberres.git
  # or if repo requires a ssh key instead of password
  git clone git@github.ibm.com:efarr/agentic-ai-cyberres.git

  # change into working directory
  cd agentic-ai-cyberres
</code></pre> 

1. Setup node.js

<code>  nvm install
</code>

2. Install dependencies

<code>  npm ci
</code>


3. Copy .env.template to .env
<code>  cp .env.template .env
</code>

4. Update .env to set your LLM provider and related settings.  

See ibm.com/watsonx to try watsonx for free, which will also provide a project ID and API key.  You choose which region to usa.
If using watsonx, set the API key and watsonx project, and other watsonx settings below:
<code>  
LLM_BACKEND="watsonx"

## WatsonX
WATSONX_API_KEY=""
WATSONX_PROJECT_ID=""
WATSONX_MODEL="ibm/granite-3-8b-instruct"
WATSONX_REGION="us-south"
</code>


5. Update .env to set the environment variables used by the agent's tools:
<code> 
# Variables for agentic-ai-cyberres data validation agent and tools
# set email address used by tool to send email
USER_EMAIL=""

# set mongoDB name and collection for mongoDB validation tool
MONGO_DB_CONN_STRING="mongodb://localhost"
MONGODB_NAME=""
MONGODB_COLLECTION_NAME=""
</code>
   
# Using agentic-ai-cyberres agent
<code> 
# to run interactively
npm run start src/agent.ts

# to run autonomousley (e.g. through cron, ansible)
npm run start src/agent.ts <<< "Check if mongoDB is running and if so, validate the mongoDB database by passing in mongondb as a parameter"
</code>

