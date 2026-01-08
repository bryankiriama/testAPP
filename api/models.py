from config.database_config import Base
from sqlalchemy_utils import Timestamp
from sqlalchemy import Column, Integer, func, String, DateTime
from sqlalchemy.orm import declared_attr


class AbstractBaseModel(Base, Timestamp):
    __abstract__ = True

    @declared_attr
    def id(cls):
        return Column(Integer, primary_key=True, index=True)


class User(AbstractBaseModel):
    __tablename__ = "users"

    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=False, default="user")  # user, admin
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

