from abc import ABC, abstractmethod
from typing import Optional
from src.domain.entities.user import User


class IUserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> User:
        """Salva ou atualiza um usuário"""
        pass

    @abstractmethod
    def find_by_email(self, email: str) -> Optional[User]:
        """Busca usuário por email"""
        pass

    @abstractmethod
    def find_by_id(self, user_id: int) -> Optional[User]:
        """Busca usuário por ID"""
        pass

    @abstractmethod
    def delete(self, user_id: int) -> None:
        """Remove usuário por ID"""
        pass

    @abstractmethod
    def update(self, user_data: User) -> User:
        """Atualiza dados do usuário"""
        pass
