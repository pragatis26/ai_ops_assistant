class ExecutorAgent:
    def __init__(self, tools: dict):
        self.tools = tools

    def execute(self, plan: dict) -> dict:
        results = []

        for step in plan["steps"]:
            tool_name = step["tool"]
            tool = self.tools.get(tool_name)

            if not tool:
                results.append({"error": f"Tool {tool_name} not found"})
                continue

            params = {k: v for k, v in step.items() if k != "tool"}
            output = tool(**params)

            results.append({
                "tool": tool_name,
                "output": output
            })

        return {"results": results}
