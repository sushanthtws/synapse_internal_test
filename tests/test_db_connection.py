import pytest
from app.db.database import db


def test_db_connection():
    engine = db.get_engine()

    with engine.connect() as conn:
        result = conn.exec_driver_sql("SELECT 1")
        assert result.scalar() == 1