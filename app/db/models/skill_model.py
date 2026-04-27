from sqlalchemy import Column, String, Text
from app.db.base import Base
import uuid


class Skill(Base):
    __tablename__ = "skills"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))

    title = Column(String)
    summary = Column(Text)

    content_hash = Column(String, unique=True, index=True)

    file_path = Column(String)
    raw_markdown = Column(Text)