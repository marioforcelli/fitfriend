from dataclasses import dataclass
from typing import Optional


@dataclass
class UserProfile:
    user_id: int
    weight: float
    height: float
    goal: str
    is_active: bool = True
    tdee: Optional[float] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
