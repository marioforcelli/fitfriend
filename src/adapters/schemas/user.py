from pydantic import BaseModel, EmailStr, BeforeValidator
from typing import Annotated
from pydantic_extra_types.phone_numbers import PhoneNumber, PhoneNumberValidator
from datetime import date

class UserCreateSchema(BaseModel):
    full_name: str
    email: EmailStr
    phone: Annotated[PhoneNumber, PhoneNumberValidator(default_region="BR")]
    weight: float
    height: float
    birth_date: date

class UserResponseSchema(BaseModel):
    email: EmailStr
    birth_date: date
