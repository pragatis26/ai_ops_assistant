import os
from groq import Groq

class LLMClient:
    def __init__(self):
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def complete(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.2
        )
        return response.choices[0].message.content
