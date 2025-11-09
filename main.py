from fastapi import FastAPI
from database import Base, engine
from routers.auth_google import router as google_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(google_router, prefix="/auth")


# 간단한 헬스체크
@app.get("/")
def ping():
    return {"ok": True}
