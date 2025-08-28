from pydantic import BaseModel
from pydantic.generics import GenericModel
from typing import Optional, Generic, TypeVar

T = TypeVar("T", bound=BaseModel)


class ResponseSchema(GenericModel, Generic[T]):
    success: bool
    error: Optional[str] = None
    data: Optional[T] = None
