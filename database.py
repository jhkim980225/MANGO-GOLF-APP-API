# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# 예: 유저 root / 비번 1234 / DB명 mango / 포트 3306
DB_URL = "mysql+pymysql://root:zzjhkim12!@127.0.0.1:3306/mango?charset=utf8mb4"

engine = create_engine(DB_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
