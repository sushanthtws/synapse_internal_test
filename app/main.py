import uuid
from fastapi import FastAPI, UploadFile, File
from sqlalchemy import text

from app.db.database import db
from app.db.models.skill_model import Skill
from app.db.models.tag_model import Tag
from app.ai.skill_normalizer import SkillNormalizer

app = FastAPI()


# =========================
# HEALTH CHECK
# =========================
@app.get("/")
def health():
    return {"status": "ok"}


# =========================
# GET ALL SKILLS
# =========================
@app.get("/skills")
def get_skills():
    session = db.get_session()

    skills = session.query(Skill).all()

    result = []
    for s in skills:
        result.append({
            "id": s.id,
            "title": s.title,
            "description": s.summary,
            "tags": [],   # can be enhanced later with join query
            "tech": [],
            "verified": True,
            "platform": "Platform Security Guild",
            "version": "v1.0"
        })

    return result


# =========================
# GET SINGLE SKILL
# =========================
@app.get("/skills/{skill_id}")
def get_skill(skill_id: str):
    session = db.get_session()

    skill = session.query(Skill).filter(Skill.id == skill_id).first()

    if not skill:
        return {"error": "not found"}

    return {
        "id": skill.id,
        "title": skill.title,
        "raw_markdown": skill.raw_markdown
    }


# =========================
# UPLOAD + AI PROCESSING
# =========================
@app.post("/upload-md")
def upload_md(file: UploadFile = File(...)):
    content = file.file.read().decode("utf-8")

    # -------------------------
    # AI NORMALIZATION
    # -------------------------
    normalizer = SkillNormalizer()
    structured = normalizer.normalize(content)

    session = db.get_session()

    # -------------------------
    # CREATE SKILL
    # -------------------------
    skill = Skill(
        id=str(uuid.uuid4()),
        title=structured["title"],
        summary=structured["description"],
        content_hash=str(uuid.uuid4()),
        file_path=file.filename,
        raw_markdown=content
    )

    session.add(skill)
    session.commit()

    # -------------------------
    # TAGGING SYSTEM
    # -------------------------
    for tag_name in structured["tags"]:

        tag = session.query(Tag).filter(Tag.id == tag_name).first()

        if not tag:
            tag = Tag(id=tag_name, name=tag_name)
            session.add(tag)
            session.commit()

        session.execute(
            text(
                "INSERT INTO skill_tags (skill_id, tag_id) VALUES (:sid, :tid)"
            ),
            {"sid": skill.id, "tid": tag_name}
        )

    session.commit()

    return {
        "status": "success",
        "skill_id": skill.id,
        "structured": structured
    }


# =========================
# SCORE ENDPOINT (PLACEHOLDER)
# =========================
@app.get("/skills/{skill_id}/score")
def score(skill_id: str):
    return {
        "skill_id": skill_id,
        "score": 1
    }