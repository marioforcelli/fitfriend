from src.domain.repositories.user_repository import IUserRepository
from domain.entities.user import User
from src.infra.db.db_config import Database


class UserRepository(IUserRepository):
    def __init__(self) -> None:
        self.db = Database()

        if self.db.connection is None:
            raise ConnectionError("Failed to connect to the database")

    def save(self, user: User) -> User:

        query = "INSERT INTO users (name, email, weight, height, birth_date, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id;"
        params = (
            user.name,
            user.email,
            user.weight,
            user.height,
            user.birth_date,
            user.created_at,
            user.updated_at,
        )
        user.id = self.db.execute_query(query, params)[0][0]
        return user

    def find_by_email(self, email: str) -> User | None:
        query = "SELECT * FROM users WHERE email = %s;"
        params = (email,)
        result = self.db.execute_query(query, params)
        if result:
            return User(**result[0])
        return None

    def find_by_id(self, user_id: int) -> Optional[User]:
        pass

    def delete(self, user_id: int) -> None:
        pass
