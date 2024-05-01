# from typing import Annotated
# from fastapi import APIRouter, Path, Query, HTTPException, Depends
# from sqlalchemy.orm import Session
# from starlette import status
# # from app import auth
# from models import Item
# from schemas.items import ItemCreate, ItemUpdate, ItemResponse
# from schemas.auth import Token,DecodedToken
# from db import get_db
# import pytz
# from datetime import datetime
# from cruds import auth

# DbDependency = Annotated[Session, Depends(get_db)]
# UserDependency = Annotated[DecodedToken, Depends(auth.get_current_user)]

# router = APIRouter(prefix="/items", tags=["Items"])

# @router.get('/items',response_model=list[ItemResponse],status_code=status.HTTP_200_OK)
# async def queryParam(db: DbDependency):
#     item = db.query(Item).all()
#     return item

# @router.get("/{id}", response_model=ItemResponse, status_code=status.HTTP_200_OK)
# async def find_by_id(db: DbDependency, user: UserDependency, id: int = Path(gt=0)):
#     found_item = db.query(Item).filter(Item.id == id).first()
#     # found_item = item.find_by_id(db, id, user.user_id)

#     if not found_item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return found_item

# #認証期限を返すよ。認証日+30で設定
# @router.get("/test_auth/{id}",status_code=status.HTTP_200_OK)
# async def find_by_id(db: DbDependency, user: UserDependency, id: int = Path(gt=0)):
#     jst_timezone = pytz.timezone('Asia/Tokyo')
#     return user.user_id,user.username,user.expires.astimezone(jst_timezone)
#     # return user.user_id
# # @router.get("/{id}", response_model=ItemResponse, status_code=status.HTTP_200_OK)
# # async def find_by_id(db: DbDependency, id: int = Path(gt=0)):
# #     found_item = db.query(Item).filter(Item.id == id).first()
# #     return found_item


# # @router.get("/", response_model=list[ItemResponse], status_code=status.HTTP_200_OK)
# # async def find_by_name(
# #     db: DbDependency, name: str = Query(min_length=2, max_length=20)
# # ):
# #     return item_cruds.find_by_name(db, name)


# # @router.post("", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
# # async def create(db: DbDependency, user: UserDependency, item_create: ItemCreate):
# #     return item_cruds.create(db, item_create, user.user_id)


# # @router.put("/{id}", response_model=ItemResponse, status_code=status.HTTP_200_OK)
# # async def update(
# #     db: DbDependency,
# #     user: UserDependency,
# #     item_update: ItemUpdate,
# #     id: int = Path(gt=0),
# # ):
# #     updated_item = item_cruds.update(db, id, item_update, user.user_id)
# #     if not updated_item:
# #         raise HTTPException(status_code=404, detail="Item not updated")
# #     return updated_item


# # @router.delete("/{id}", response_model=ItemResponse, status_code=status.HTTP_200_OK)
# # async def delete(db: DbDependency, user: UserDependency, id: int = Path(gt=0)):
# #     deleted_item = item_cruds.delete(db, id, user.user_id)
# #     if not deleted_item:
# #         raise HTTPException(status_code=404, detail="Item not deleted")
# #     return deleted_item
