from sqlalchemy import Column, String
from app.db.base import Base


class Tag(Base):
    __tablename__ = "tags"

    id = Column(String, primary_key=True)   # e.g. "python"
    name = Column(String, unique=True)