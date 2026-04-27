from sqlalchemy import Column, String, ForeignKey
from app.db.base import Base


class SkillTag(Base):
    __tablename__ = "skill_tags"

    skill_id = Column(String, ForeignKey("skills.id"), primary_key=True)
    tag_id = Column(String, ForeignKey("tags.id"), primary_key=True)