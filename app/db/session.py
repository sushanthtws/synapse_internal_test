from sqlalchemy.orm import sessionmaker
from app.db.database import db


class SessionLocal:
    def __init__(self):
        self._session_maker = sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=db.get_engine(),
        )

    def get_session(self):
        return self._session_maker()