from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    # 이메일은 최대 255로 충분
    email = Column(String(255), unique=True, index=True, nullable=False)

    # username도 길면 100 이하로 충분
    username = Column(String(100), unique=True, index=True, nullable=False)

    # hashed_password는 bcrypt이면 60~200 길이까지 가능
    hashed_password = Column(String(255), nullable=True)

    # 구글 로그인은 password 없이 생성되므로 nullable=True 처리해야 함!
    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
