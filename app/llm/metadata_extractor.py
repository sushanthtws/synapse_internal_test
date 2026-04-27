import json
from app.llm.llm_manager import LLMManager


class MetadataExtractor:
    def __init__(self):
        self.llm = LLMManager()

    def extract(self, data: dict) -> dict:
        prompt = self._build_prompt(data)

        response = self.llm.generate(prompt)

        return self._parse_response(response)

    def _build_prompt(self, data: dict) -> str:
        return f"""
You are a metadata extraction engine.

Extract structured metadata from the following skill document.

Return ONLY valid JSON with keys:
title, summary, author, tags, tech, domain

Rules:
- tags must be normalized (no duplicates, lowercase)
- tech = programming/tools/stack
- domain = industry area
- summary must be 2-3 lines max

INPUT:
{json.dumps(data, indent=2)}

OUTPUT:
"""

    def _parse_response(self, response: str) -> dict:
        try:
            data = json.loads(response)
        except Exception:
            return {
                "title": "",
                "summary": response[:200],
                "author": "",
                "tags": [],
                "tech": [],
                "domain": []
            }

        return {
            "title": data.get("title", ""),
            "summary": data.get("summary", ""),
            "author": data.get("author", ""),
            "tags": self._ensure_list(data.get("tags", [])),
            "tech": self._ensure_list(data.get("tech", [])),
            "domain": self._ensure_list(data.get("domain", [])),
        }

    def _ensure_list(self, value):
        if value is None:
            return []
        if isinstance(value, list):
            return value
        return [value]

    def _ensure_list(self, value):
        if value is None:
            return []
        if isinstance(value, list):
            return value
        return [value]