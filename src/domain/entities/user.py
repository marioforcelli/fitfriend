from dataclasses import dataclass


@dataclass
class User:
    id: int | None
    name: str
    email: str
    weight: float
    height: float
    birth_date: str
    created_at: str
    updated_at: str
