"# Mango Golf App API" 
- Fast API 테스트 입니다.


# requirements.txt
- pip install -r requirements.txt

# project run
- uvicorn main:app --reload



- api/ : FastAPI 라우트를 버전별로 정리 (v1/users.py 등)
- crud/ : 데이터베이스 접근 로직 (repository 패턴 유사)
- models/ : SQLAlchemy ORM 모델
- schemas/ : 요청/응답용 Pydantic 스키마
- core/ : 설정 및 공통 기능 (보안, 환경변수 등)
- db/ : DB 세션 생성 및 초기화, Alembic 연동
- main.py : FastAPI 앱 실행 진입점

# JWT 시크릿키 생성
- python -c "import secrets; print(secrets.token_hex(32))"
- 서버에서 발급해주는 키 ( 키젠으로 생성해도 됨. )

# https://www.jwt.io/
- JWT 구조를 확인하고 디코딩 하는 사이트 ( 학습 / 검증 용)
- JWT 토큰을 붙여넣으면 headers / payload / signature 분리 됨

header
payload (유저 정보, exp, sub 등)
signature

- Base64로 인코딩된 JWT 내용을 사람이 읽을 수 있게 보여주는 역할
{
  "sub": "104780559455825273158",
  "email": "jhkimgpt4@gmail.com",
  "exp": 1762411231
}

