from datetime import date
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict

class ItemStatus(Enum):
    man = "男"
    woman = "女"
         
class UserCreate(BaseModel):
    company_id: int = Field(gt=0, examples=[1])
    department_id: int = Field(gt=0, examples=[1])
    user_name: str = Field(min_length=2, examples=["Walls太郎"])
    name_kana: str = Field(min_length=2, examples=["うぉーるずたろう"])
    password: str = Field(min_length=8, examples=["test1234"])
    email: str = Field(min_length=8, examples=["test@walls-inc.com"])
    storage: int = Field(gt=1, examples=[5])
    permission: bool = Field()
    admin: bool = Field()

class UserAll(BaseModel):
    id: int = Field(gt=0, examples=[1])
    company_id: int = Field(gt=0, examples=[1])
    department_id: int = Field(gt=0, examples=[1])
    user_name: str = Field(min_length=2, examples=["Walls太郎"])
    name_kana: str = Field(min_length=2, examples=["うぉーるずたろう"])
    password: str = Field(min_length=8, examples=["test1234"])
    email: str = Field(min_length=8, examples=["test@walls-inc.com"])
    storage: int = Field(gt=5, examples=[1])
    salt: str = Field()
    age: date = Field(examples=['1999-01-01'])
    sex: Optional[ItemStatus] = Field(None, examples=[ItemStatus.man])
    permission: bool = Field()
    admin: bool = Field()

class UserResponse(BaseModel):
    user_name: str = Field(min_length=2, examples=["Walls太郎"])
    email: str = Field(min_length=8, examples=["test@walls-inc.com"])
    storage: int = Field(gt=1, examples=[5])
    # model_config = ConfigDict(from_attributes=True)