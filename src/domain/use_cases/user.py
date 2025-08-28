from abc import ABC, abstractmethod
from typing import Optional
from src.domain.entities.user import User


class IUserUseCase(ABC):

    @abstractmethod
    def get_user_by_email(self, email: str) -> Optional[User]:
        """Busca usuário por email"""
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        """Busca usuário por ID"""
        pass

    @abstractmethod
    def create_user(self, user_data: User) -> User:
        """Cria novo usuário"""
        pass

    @abstractmethod
    def update_user(self, user_data: User) -> User:
        """Atualiza usuário existente"""
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> None:
        """Remove usuário"""
        pass
