from app.db.repositories.skill_repository import SkillRepository
from app.db.session import SessionLocal


def test_skill_insert_and_fetch():
    session = SessionLocal().get_session()
    repo = SkillRepository(session)

    skill_data = {
        "id": "test-id",
        "title": "PDF Skill",
        "summary": "Handles PDF processing",
        "content_hash": "abc123",
        "file_path": "data/skills/sample.md",
        "raw_markdown": "# PDF Skill"
    }

    repo.create(skill_data)

    result = repo.get_by_hash("abc123")

    assert result is not None
    assert result.title == "PDF Skill"
