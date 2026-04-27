from app.ingestion.ingestion_pipeline import IngestionPipeline
from app.db.session import SessionLocal
from app.db.repositories.skill_repository import SkillRepository
import os

def test_full_ingestion_pipeline():
    folder_path = os.path.abspath("data/skills")
    session = SessionLocal().get_session()
    repo = SkillRepository(session)

    pipeline = IngestionPipeline()
    result = pipeline.run(folder_path)

    assert result["processed"] >= 1

    skills = repo.get_all()
    assert len(skills) >= 1

    assert skills[0].content_hash is not None