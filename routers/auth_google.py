# routers/auth_google.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import GoogleLoginRequest, GoogleLoginResponse, UserResponse
from services.auth_service import google_login


router = APIRouter()


@router.post("/google", response_model=GoogleLoginResponse)
def google_auth(req: GoogleLoginRequest, db: Session = Depends(get_db)):
    result, error = google_login(req.id_token, db)

    if error:
        raise HTTPException(status_code=400, detail=error)

    return {
        "access_token": result["access_token"],
        "token_type": "bearer",
        "user": UserResponse.model_validate(result["user"])
    }
