AI Operations Assistant – GenAI Intern Assignment
Overview

The AI Operations Assistant is a multi-agent system that accepts a natural-language task, plans steps, calls tools (APIs), and returns a structured result. It demonstrates agent-based reasoning, LLM usage, and integration with real-world APIs.

Core Agents:

Planner Agent – Converts user tasks into a JSON plan with steps and required tools.

Executor Agent – Executes the planned steps by calling the registered APIs.

Verifier Agent – Validates and cleans the results, ensuring completeness and correctness.

Integrated APIs:

GitHub API → Search repositories and fetch stars, URLs, and names.

OpenWeatherMap API → Fetch current weather by city.

Project Structure
ai_ops_assistant/
├── agents/
│   ├── planner.py       # Planner Agent
│   ├── executor.py      # Executor Agent
│   └── verifier.py      # Verifier Agent
├── tools/
│   ├── github.py        # GitHub search tool
│   └── weather.py       # Weather lookup tool
├── llm/
│   └── client.py        # LLM client (OpenAI GPT)
├── main.py              # FastAPI entrypoint
├── requirements.txt
├── .env.example
└── README.md

Setup Instructions

Clone the repository

git clone <your_repo_url>
cd ai_ops_assistant


Install dependencies

pip install -r requirements.txt


Setup environment variables

Create .env based on .env.example:

OPENAI_API_KEY=your_openai_key_here
OPENWEATHER_API_KEY=your_openweather_key_here


Run the project locally

uvicorn main:app --reload


Access API docs: http://127.0.0.1:8000/docs

Usage / Example Prompts

Endpoint: POST /run
Request Body:

{
  "task": "Find popular Python repositories and current weather in Mumbai"
}


Sample Response:

{
  "task": "Find popular Python repositories and current weather in Mumbai",
  "plan": {
    "steps": [
      {"tool": "github_search", "query": "python"},
      {"tool": "weather_lookup", "city": "Mumbai"}
    ]
  },
  "result": {
    "results": [
      {
        "tool": "github_search",
        "output": [
          {"name": "donnemartin/system-design-primer", "stars": 334473, "url": "..."},
          {"name": "vinta/awesome-python", "stars": 281523, "url": "..."}
        ]
      },
      {
        "tool": "weather_lookup",
        "output": {"city": "Mumbai", "temperature": 30.99, "description": "smoke"}
      }
    ]
  }
}


Other Example Prompts:

"Get trending JavaScript repos and weather in Delhi"

"List top machine learning repos on GitHub and current weather in Bangalore"

"Find Python beginner projects and Mumbai weather"

Architecture Explanation
User Task → Planner Agent → JSON Plan → Executor Agent → API Calls → Verifier Agent → Final Output


Planner – Uses OpenAI LLM to produce structured steps.

Executor – Executes tools registered in tools/ folder.

Verifier – Validates outputs, removes incomplete data, ensures schema compliance.

Known Limitations / Tradeoffs

API calls are sequential; no parallel execution (may affect latency).

LLM output depends on OpenAI API; small chance of invalid JSON if model fails.

Rate limits apply for GitHub and OpenWeather APIs.

No caching implemented; repeated tasks will call APIs every time.

Environment Variables (.env.example)
OPENAI_API_KEY=your_openai_key_here
OPENWEATHER_API_KEY=your_openweather_key_here


This README covers all TrulyMadly submission requirements: setup instructions, architecture, APIs, prompts, limitations, and running instructions.