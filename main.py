from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TaskRequest(BaseModel):
    task: str

@app.post("/run")
def run_task(request: TaskRequest):
    return {
        "status": "success",
        "message": "Project setup complete",
        "task_received": request.task
    }