# from datetime import datetime, timedelta
# from typing import Annotated
# from fastapi import Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer
# from jose import jwt, JWTError
# from schemas.auth import DecodedToken

# oauth2_schema = OAuth2PasswordBearer(tokenUrl="/auth/login")
# #アクセストークンの作成
# #ハッシュ化の方法
# ALGORITHM = "HS256"
# #ランダムな値
# SECRET_KEY = "aaaaaaiuhlciakycbkaybciluabufchnlhaullbnubn1111u;h;uoho;h3uoh3;ounh"

# def create_access_token(username: str, user_id: int, expires_delta: timedelta):
#     expires = datetime.now() + expires_delta
#     payload = {"name": username, "id": user_id, "exp": expires}
#     return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

# def get_current_user(token: Annotated[str, Depends(oauth2_schema)]):
#     #ユーザ名orユーザidの不備で認証不可
#     authorization_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate authorization",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     #資格情報無しorアクセストークンの期限切れ
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username = payload.get("name")
#         user_id = payload.get("id")
#         expires = payload.get("exp")
#         if username is None or user_id is None:
#             return authorization_exception
#         return DecodedToken(username=username, user_id=user_id, expires=expires)
#     except JWTError:
#         raise credentials_exception
