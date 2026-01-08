from passlib.context import CryptContext
# from test.config.database_config import SessionLocal
from config.database_config import SessionLocal

pwd_context = CryptContext(schemes=["sha256_crypt"])



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_hashed_password(password: str):
    return pwd_context.hash(password)