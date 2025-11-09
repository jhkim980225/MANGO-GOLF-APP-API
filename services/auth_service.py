# services/auth_service.py

from google.oauth2 import id_token
from google.auth.transport import requests
from sqlalchemy.orm import Session
from core.config import settings
from core.security import create_jwt
from models import User


def google_login(id_token_str: str, db: Session):
    try:
        # ✅ 구글 idToken 검증
        info = id_token.verify_oauth2_token(
            id_token_str,
            requests.Request(),
            settings.GOOGLE_CLIENT_ID
        )
    except Exception:
        return None, "Invalid ID Token"

    email = info.get("email")
    name = info.get("name") or email.split("@")[0]

    # ✅ DB에서 사용자 조회
    user = db.query(User).filter(User.email == email).first()

    # ✅ 최초 로그인 → 회원가입 처리
    if not user:
        user = User(
            email=email,
            username=name,
            hashed_password=None,
            is_active=True
        )
        db.add(user)
        db.commit()
        db.refresh(user)

    # ✅ JWT 발급
    token = create_jwt({
        "sub": user.email,
        "user_id": user.id
    })

    return {
        "access_token": token,
        "token_type": "bearer",
        "user": user
    }, None
