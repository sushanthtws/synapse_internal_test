from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config.settings import settings


class Database:
    def __init__(self):
        self._engine = None
        self._SessionLocal = None

    def get_engine(self):
        if self._engine is None:
            self._engine = create_engine(
                settings.get_database_url(),
                echo=True
            )
        return self._engine

    def get_session_factory(self):
        if self._SessionLocal is None:
            self._SessionLocal = sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self.get_engine()
            )
        return self._SessionLocal

    def get_session(self):
        SessionLocal = self.get_session_factory()
        return SessionLocal()


db = Database()