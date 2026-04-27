from app.db.database import db
from app.db.base import Base
from app.db.models.skill_model import Skill


def reset():
    engine = db.get_engine()
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    print("DB reset complete")


if __name__ == "__main__":
    reset()