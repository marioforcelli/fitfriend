from pydantic import BaseModel, EmailStr


class UserCreateSchema(BaseModel):
    full_name: str
    email: EmailStr
    weight: float
    height: float
    birth_date: str


class UserResponseSchema(BaseModel):
    email: EmailStr
    birth_date: str
