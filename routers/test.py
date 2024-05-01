from fastapi import Depends, APIRouter, FastAPI, HTTPException,status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWSError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
# from models import Item, User
from models import Company, User
# from schemas.items import ItemCreate,ItemUpdate,ItemResponse
# from schemas.users import UserCreate,UserResponse
from sqlalchemy.orm import session
from typing import Annotated
# from db import session  # DBと接続するためのセッション
# from pydantic import BaseModel
# from sqlalchemy.orm import Session
from db import get_db
from sqlalchemy.orm import Session

DbDependency = Annotated[Session, Depends(get_db)]

router = APIRouter(prefix="/tst",tags=["tests"])
@router.get('/items',status_code=status.HTTP_200_OK)
async def queryParam(db: DbDependency):
    item = db.query(Company).all()
    return item

@router.get('/users',status_code=status.HTTP_200_OK)
async def queryParam(db: DbDependency):
    item = db.query(User).all()
    return item

# @router.get('/items2', response_model=ItemResponse,status_code=status.HTTP_201_CREATED)
# async def queryParam():
#     item = session.query(Item).first()
#     return item

# @router.get("/items3", response_model=list[ItemResponse], status_code=status.HTTP_200_OK)
# async def find_all():
#     item = session.query(Item).all()
#     return item
