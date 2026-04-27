import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db.database import db
from app.db.base import Base
from app.db.models.skill_model import Skill


def init():
    engine = db.get_engine()
    Base.metadata.create_all(engine)
    print("DB initialized successfully")


if __name__ == "__main__":
    init()