from sentence_transformers import SentenceTransformer
import re


class SkillNormalizer:
    """
    Converts raw markdown → structured skill product card.
    """

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def normalize(self, content: str) -> dict:
        return {
            "title": self.generate_title(content),
            "verified": True,
            "platform": "Platform Security Guild",
            "version": "v1.0",
            "description": self.generate_description(content),
            "tech": self.extract_tech(content),
            "tags": self.generate_tags(content),
            "domain": self.detect_domain(content)
        }

    # -------------------------
    # TITLE (AI-ish heuristic)
    # -------------------------
    def generate_title(self, text: str):
        # try first heading
        match = re.search(r"#\s+(.*)", text)
        if match:
            return match.group(1).strip()

        return "Skill Module"

    # -------------------------
    # DESCRIPTION
    # -------------------------
    def generate_description(self, text: str):
        sentences = text.split(".")
        return sentences[0][:160].strip()

    # -------------------------
    # TECH STACK EXTRACTION
    # -------------------------
    def extract_tech(self, text: str):
        tech_keywords = [
            "react", "fastapi", "python", "docker",
            "postgres", "kubernetes", "aws", "mongodb"
        ]

        found = []
        lower = text.lower()

        for t in tech_keywords:
            if t in lower:
                found.append(t.capitalize())

        return found

    # -------------------------
    # TAG GENERATION
    # -------------------------
    def generate_tags(self, text: str):
        tags = []

        mapping = {
            "auth": "authentication jwt login security",
            "rbac": "role based access control permissions",
            "etl": "data pipeline ingestion transformation",
            "api": "rest graphql api backend",
            "security": "security encryption auth"
        }

        lower = text.lower()

        for tag, keywords in mapping.items():
            if any(k in lower for k in keywords.split()):
                tags.append(tag)

        return list(set(tags))

    # -------------------------
    # DOMAIN DETECTION
    # -------------------------
    def detect_domain(self, text: str):
        if "auth" in text.lower() or "security" in text.lower():
            return "Backend Security"

        if "ui" in text.lower() or "react" in text.lower():
            return "Frontend"

        if "etl" in text.lower():
            return "Data Engineering"

        return "General Engineering"