# Load environment variables
from dotenv import load_dotenv
load_dotenv()


# FastAPI imports
from fastapi import FastAPI
from pydantic import BaseModel

# Agents & Tools
from llm.client import LLMClient
from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent
from agents.verifier import VerifierAgent

from tools.github import github_search
from tools.weather import weather_lookup

# Initialize FastAPI
app = FastAPI(title="AI Ops Assistant")

# -------- Request Schema --------
class TaskRequest(BaseModel):
    task: str

# -------- API Endpoint --------
@app.post("/run")
def run_task(request: TaskRequest):
    try:
        # 1️⃣ Initialize LLM + Planner
        llm = LLMClient()
        planner = PlannerAgent(llm)

        # 2️⃣ Generate plan from natural language task
        plan = planner.plan(request.task)

        # 3️⃣ Register tools
        tools = {
            "github_search": github_search,
            "weather_lookup": weather_lookup
        }

        # 4️⃣ Execute plan
        executor = ExecutorAgent(tools)
        execution_result = executor.execute(plan)

        # 5️⃣ Verify execution results
        verifier = VerifierAgent()
        final_result = verifier.verify(execution_result)

        # 6️⃣ Return task, plan, and verified result
        return {
            "task": request.task,
            "plan": plan,
            "result": final_result
        }

    except Exception as e:
        return {"error": str(e)}

# -------- Optional: debug print for env vars --------
import os
print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))
print("OPENWEATHER_API_KEY:", os.getenv("OPENWEATHER_API_KEY"))
