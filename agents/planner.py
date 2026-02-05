import json

class PlannerAgent:
    def __init__(self, llm_client):
        self.llm_client = llm_client

    def plan(self, task: str) -> dict:
        prompt = f"""
You are a Planner Agent.

Convert the user task into a step-by-step execution plan.
Return ONLY valid JSON. No explanations.

Available tools:
- github_search (search GitHub repositories)
- weather_lookup (get current weather by city)

User task:
{task}

Output JSON format:
{{
  "steps": [
    {{
      "tool": "github_search",
      "query": "python"
    }},
    {{
      "tool": "weather_lookup",
      "city": "Mumbai"
    }}
  ]
}}
"""
        response = self.llm_client.complete(prompt)
        return json.loads(response)
