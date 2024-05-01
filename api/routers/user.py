# from fastapi import Depends, APIRouter, FastAPI, HTTPException,status
# from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
# from jose import JWSError, jwt
# from passlib.context import CryptContext
# from pydantic import BaseModel
# # from models.item import Item, ItemTable
# # from models.user import User, UserTable
# from sqlalchemy.orm import session
# from typing import List  # ネストされたBodyを定義するために必要
# from db import session  # DBと接続するためのセッション
# from pydantic import BaseModel

# router = APIRouter(prefix="/tst",tags=["tests"])

# @router.get('/item')
# async def queryParam():
#     item = session.query(ItemTable).all()
#     return item

# @router.post("/updateitem")
# async def queryParam(items: List[Item]):
#     update_item = items[0]
#     item = session.query(ItemTable)\
#        .filter(ItemTable.id == update_item.id)\
#        .first()
#     item.name = update_item.name
#     item.price = update_item.price
#     session.commit()
#     item = session.query(ItemTable)\
#        .filter(ItemTable.id == update_item.id)\
#        .first()
#     return item


# @router.get('/user')
# async def queryParam(email: str,password: str):
#     user = session.query(UserTable)\
#                 .filter(UserTable.email == email)\
#                 .all()
#     return user

# @router.post("/user")
# # クエリでnameとstrを受け取る
# # /user?name="三郎"&age=10
# async def create_user(Item:User):
#     user = UserTable()
#     user.name = Item.name
#     user.age = Item.age
#     session.add(user)
#     session.commit()
#     return user
# # 複数のユーザ情報を更新 PUT


# @router.put("/users")
# # modelで定義したUserモデルのリクエストbodyをリストに入れた形で受け取る
# # users=[{"id": 1, "name": "一郎", "age": 16},{"id": 2, "name": "二郎", "age": 20}]
# async def update_users(users: List[User]):
#     for new_user in users:
#         user = session.query(UserTable).\
#             filter(UserTable.id == new_user.id).first()
#         user.name = new_user.name
#         user.age = new_user.age
#         session.commit()

# @router.post("/user/")
# async def post_user(item:User):
#     for i in range(1,5):
#         user = UserTable()
#         user.name = i
#         user.age = i
#         session.add(user)
#     session.commit()
#     # user.name = item.name
#     # user.age = item.age
#     # session.add(user)
#     # session.commit()

# @router.get('/user/count')
# async def count_test():
#     user = session.query(UserTable).filter(UserTable.id == 1).all()
#     return user

# @router.get('/usertest')
# async def queryParam(email: str,password: str):
#     user = session.query(UserTable)\
#                 .filter(UserTable.email == email)\
#                 .first()
#     if not user: 
#         return 'アカウントが登録されていません。'
#     if user.password != password:
#         return 'パスワードが間違っています。'        
#     return user.name + '君、認証します。'

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# @router.get("items/")
# async def read_items(token: str = Depends(oauth2_scheme)):
#     return {"token":token}