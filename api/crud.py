from sqlalchemy.orm import Session
from .schemas import UserCreate
from .models import User
from .utils import get_hashed_password

def create_user(db: Session, user: UserCreate):
  hashed_password = get_hashed_password(user.password)
  db_user = User(
      username=user.username,
      email=user.email,
      password_hash=hashed_password,
      role=user.role
  )
  db.add(db_user)
  db.commit()
  db.refresh(db_user)
  return db_user

def get_user_by_username(db: Session, username: str):
  return db.query(User).filter(User.username == username).first()

def get_user_by_email(db: Session, email: str):
  return db.query(User).filter(User.email == email).first()



def get_user_by_email(db: Session, email: str):
  return db.query(User).filter(User.email == email).first()
