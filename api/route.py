from fastapi import APIRouter, HTTPException, Depends
from .schemas import UserCreate,UserRead
from .utils import get_db
from .crud import get_user_by_username, get_user_by_email, create_user
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/register", response_model=UserRead)
def register(user: UserCreate , db: Session = Depends(get_db)):
    if get_user_by_username(db, user.username) or get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="User already exists")
    return create_user(db, user)
