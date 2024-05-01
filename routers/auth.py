from datetime import timedelta
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from sqlalchemy.orm import Session
from starlette import status
from schemas.users import UserCreate,UserResponse
from schemas.auth import Token,DecodedToken
# from app import auth
from db import get_db
from models import User
import hashlib
import base64
import os
from datetime import timedelta
from auth import create_access_token,get_current_user
from datetime import datetime
DbDependency = Annotated[Session, Depends(get_db)]
FormDependency = Annotated[OAuth2PasswordRequestForm, Depends()]
router = APIRouter(prefix="/auth", tags=["Auth"])

#ユーザー作成機能
#saltとはパスワードをハッシュ化する際に使用するランダムな値
#パスワードと組み合わせてハッシュ化することで同じパスワードでも異なるハッシュ値を生成する仕組みを作る。
# @router.post("/signup", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
# async def create_user(db: DbDependency,user_create: UserCreate):
@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def create_user(db: DbDependency,user_create: UserCreate):
    salt = base64.b64encode(os.urandom(32))
    hashed_password = hashlib.pbkdf2_hmac(
        "sha256", user_create.password.encode(), salt, 1000
    ).hex()
    new_user = User(
        company_id=user_create.company_id,
        department_id=user_create.department_id,
        user_name=user_create.user_name,
        name_kana=user_create.name_kana,
        password=hashed_password,
        salt=salt.decode(),
        email=user_create.email,
        storage=user_create.storage,
        permission=user_create.permission,
        admin=user_create.admin,
        create_at= datetime.now()
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    new_user_create = UserResponse(
        user_name=new_user.user_name,
        email=new_user.email,
        storage=new_user.storage
        )
    # return datetime.now()
    return new_user_create

#ログイン機能
@router.post("/login", response_model=Token,status_code=status.HTTP_200_OK)
async def login(db: DbDependency, form_data: FormDependency):

    user = db.query(User).filter(User.username == form_data.username).first()
    #ユーザー存在チェック
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username")

    hashed_password = hashlib.pbkdf2_hmac(
        "sha256", form_data.password.encode(), user.salt.encode(), 1000
    ).hex()
    #パスワードチェック
    if user.password != hashed_password:
        raise HTTPException(status_code=401, detail="Incorrect password")

    token = auth.create_access_token(
        user.username, user.id, timedelta(days=30)
        # user.username, user.id, timedelta(minutes=5)        
    )
    return {"access_token": token, "token_type": "bearer"}

# ユーザー情報取得
@router.get('/users',status_code=status.HTTP_200_OK)
async def find_all(db: DbDependency):
    user = db.query(User).all()
    return user