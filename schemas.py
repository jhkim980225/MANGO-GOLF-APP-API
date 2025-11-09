from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# ✅ 공통 기본
class UserBase(BaseModel):
    email: EmailStr
    username: str

# ✅ 회원가입 요청
class UserCreate(UserBase):
    password: str

# ✅ 일반 로그인 요청
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# ✅ 사용자 응답
class UserResponse(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

# ✅ JWT 응답
class Token(BaseModel):
    access_token: str
    token_type: str

# ✅ 내부 토큰 파싱용
class TokenData(BaseModel):
    email: Optional[str] = None

# ✅ ⬇️⬇️ 구글 로그인 전용 추가 ⬇️⬇️
# ✅ 구글 로그인 요청(idToken 받기)
class GoogleLoginRequest(BaseModel):
    id_token: str

# ✅ 구글 로그인 응답(JWT + 사용자)
class GoogleLoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse
