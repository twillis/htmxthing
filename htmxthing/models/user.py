from sqlalchemy import (
    Column,
    Index,
    Integer,
    String,
)
from .meta import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)
