# agents/verifier.py
class VerifierAgent:
    def __init__(self):
        pass

    def verify(self, execution_result: dict) -> dict:
        verified_results = []

        for res in execution_result.get("results", []):
            tool = res.get("tool")
            output = res.get("output")

            if tool == "github_search":
                valid_repos = [r for r in output if all(k in r for k in ["name", "stars", "url"])]
                verified_results.append({"tool": tool, "output": valid_repos})

            elif tool == "weather_lookup":
                if all(k in output for k in ["city", "temperature", "description"]):
                    verified_results.append(res)

            else:
                verified_results.append(res)  # unknown tool

        return {"results": verified_results}
