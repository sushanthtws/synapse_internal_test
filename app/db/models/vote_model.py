from sqlalchemy import Column, String, Integer
from app.db.base import Base


class Vote(Base):
    __tablename__ = "votes"

    id = Column(String, primary_key=True)
    skill_id = Column(String, index=True)
    value = Column(Integer)  # +1 = upvote, -1 = downvote