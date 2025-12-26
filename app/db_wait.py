import time
from sqlalchemy import text
from sqlalchemy.exc import OperationalError
from app.database import engine

def wait_for_db(retries: int = 10, delay: int = 2):
    for attempt in range(retries):
        try:
            with engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            return
        except OperationalError:
            time.sleep(delay)
    raise RuntimeError('Database not ready after retries.')