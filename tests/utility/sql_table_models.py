from sqlalchemy import Boolean, Column, DateTime, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
  __tablename__ = "auth_user"

  id = Column(Integer, primary_key=True)
  password = Column(String)
  last_login = Column(DateTime)
  is_superuser = Column(Boolean)
  username = Column(String)
  first_name = Column(String)
  last_name = Column(String)
  is_active = Column(Boolean)