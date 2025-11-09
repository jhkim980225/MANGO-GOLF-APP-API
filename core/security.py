# core/security.py

from datetime import datetime, timedelta
from jose import jwt
from core.config import settings

# ✅ JWT 발급 함수
def create_jwt(payload: dict) -> str:
    """
    payload = {
        "sub": 구글유저ID,
        "email": 이메일,
        "name": 이름,
        ...
    }
    """

    # 현재 시간으로부터 만료 시간 설정
    expire = datetime.utcnow() + timedelta(seconds=settings.JWT_EXPIRE_SECONDS)
    payload.update({"exp": expire})

    # jwt 인코딩
    encoded = jwt.encode(
        payload,
        settings.JWT_SECRET,
        algorithm=settings.JWT_ALGORITHM,
    )

    return encoded


# ✅ JWT 검증 함수
def verify_jwt(token: str):
    try:
        decoded = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.JWT_ALGORITHM]
        )
        return decoded
    except Exception:
        return None
