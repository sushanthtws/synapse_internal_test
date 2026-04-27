from app.db.models.skill_model import Skill


class SkillRepository:
    def __init__(self, session):
        self.session = session

    def create(self, data: dict):
        try:
            skill = Skill(**data)
            self.session.add(skill)
            self.session.commit()
            self.session.refresh(skill)
            return skill

        except Exception as e:
            self.session.rollback()
            print("[REPO ERROR]", e)
            return None
    def get_by_hash(self, content_hash: str):
        return self.session.query(Skill).filter_by(
            content_hash=content_hash
        ).first()

    def get_all(self):
        return self.session.query(Skill).all()