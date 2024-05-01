from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict
         
class CompanyCreate(BaseModel):
    id: int = Field(gt=0, examples=[1])
    industry_id: int = Field(gt=0, examples=[1])
    region_id: int = Field(gt=0, examples=[1])
    company_name: str = Field(min_length=2, examples=["株式会社walls"])
    tell: str = Field(min_length=10, examples=["090-0011-2233"])
    storage: int = Field(gt=0, examples=[5])
    create_at: Optional[datetime] = Field(None) 
    update_at: Optional[datetime] = Field(None) 

class CompanyResponse(BaseModel):
    id: int = Field(gt=0, examples=[1])
    company_name: str = Field(min_length=2, examples=["株式会社walls"])
    tell: str = Field(min_length=10, examples=["090-0011-2233"])
    storage: int = Field(gt=0, examples=[5])
