from pydantic import BaseModel, EmailStr, PastDatetime
from typing import Optional


class UserCreateSchema(BaseModel):
    full_name: str
    email: EmailStr
    weight: float
    height: float
    birth_date: str


class UserResponseSchema(BaseModel):
    email: EmailStr
    birth_date: str


class FinalUserResponseSchema(BaseModel):
    success: bool
    error: Optional[str] = None
    data: Optional[UserResponseSchema] = None