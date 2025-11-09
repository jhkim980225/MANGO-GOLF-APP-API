# core/config.py

from pydantic import BaseModel

class Settings(BaseModel):
    GOOGLE_CLIENT_ID: str = "292802556475-hic2k8aitg0u3fdep7gmajr9ai7sonbf.apps.googleusercontent.com"
    JWT_SECRET: str = "664292dff8c23b8c54aa657e0edf41e5d5889cc7fc7585287c2b143767d29fbd"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_SECONDS: int = 60 * 60  # 1시간

settings = Settings()
