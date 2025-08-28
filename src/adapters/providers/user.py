from src.application.use_cases import UserUseCases
from src.infra.repositories.user_repository import UserRepository


class UserProvider:

    def __call__(self) -> UserUseCases:
        repo = UserRepository()
        return UserUseCases(repo)
