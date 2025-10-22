from dataclasses import dataclass
from typing import Optional


@dataclass
class User:
    full_name: str
    chat_id: str
    email: str
    phone: str
    birth_date: str
    updated_at: Optional[str] = None
    created_at: Optional[str] = None
    id: Optional[int] = None
