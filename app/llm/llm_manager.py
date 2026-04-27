import requests


class LLMManager:
    def __init__(self, model: str = "mistral"):
        self.model = model
        self.base_url = "http://localhost:11434/api/generate"

    def generate(self, prompt: str) -> str:
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        response = requests.post(self.base_url, json=payload)

        if response.status_code != 200:
            raise Exception(f"LLM error: {response.text}")

        return response.json()["response"]