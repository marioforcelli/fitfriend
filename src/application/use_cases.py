from src.infra.repositories.user_repository import UserRepository
from src.domain.repositories.user_repository import IUserRepository
from src.domain.entities.user import User
from src.domain.use_cases.user import IUserUseCase
from typing import Optional


class UserUseCases(IUserUseCase):
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def get_user_info(self) -> User:
        pass
        # return self.user_repository.find_by_email()

    def get_user_by_email(self, email: str) -> User | None:
        pass

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        pass

    def create_user(self, user_data: User) -> User:
        return self.user_repository.save(user_data)

    def update_user(self, user_data: User) -> User:
        pass

    def delete_user(self, user_id: int) -> None:
        pass
