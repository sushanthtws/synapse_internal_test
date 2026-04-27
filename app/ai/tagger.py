
from sentence_transformers import SentenceTransformer
import numpy as np


class AITagger:
    """
    Lightweight semantic tag generator using embeddings.
    """

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        # Controlled taxonomy (VERY IMPORTANT)
        self.known_tags = {
            "python": "python programming backend scripting",
            "java": "java spring backend enterprise",
            "go": "golang microservices backend",
            "etl": "data pipeline etl ingestion transformation",
            "frontend": "react ui frontend web",
            "backend": "api microservices backend server",
            "infra": "docker kubernetes devops aws cloud",
            "ml": "machine learning ai model training",
            "database": "sql postgres database storage"
        }

        self.tag_embeddings = {
            k: self.model.encode(v) for k, v in self.known_tags.items()
        }

    def generate_tags(self, text: str, top_k: int = 4):
        text_emb = self.model.encode(text)

        scores = []

        for tag, emb in self.tag_embeddings.items():
            score = self.cosine_similarity(text_emb, emb)
            scores.append((tag, score))

        scores.sort(key=lambda x: x[1], reverse=True)

        return [tag for tag, _ in scores[:top_k]]

    def cosine_similarity(self, a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))