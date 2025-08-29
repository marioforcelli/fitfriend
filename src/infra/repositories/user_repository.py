from src.domain.exceptions.user import UserAlreadyExistsError
from src.domain.repositories.user_repository import IUserRepository
from src.domain.entities.user import User
from src.infra.db.db_config import Database
from typing import Optional
import psycopg2
class UserRepository(IUserRepository):
    def __init__(self) -> None:
        self.db = Database()

        if self.db.connection is None:
            raise ConnectionError("Failed to connect to the database")

    def save(self, user: User) -> User:

        try:
            query = "INSERT INTO users (full_name, email, weight, height, birth_date, phone) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id;"
            params = (user.full_name, user.email, user.weight, user.height, user.birth_date, user.phone)
            self.db.execute_query(query, params)
            return user
        except psycopg2.errors.UniqueViolation:
            print("Unique constraint violated")
            raise UserAlreadyExistsError("User with this email already exists.")

    def get_user_by_email(self, email: str) -> Optional[User]:
        print(email)
        query = "SELECT * FROM users WHERE email = %s;"
        params = (email,)
        print(query, params)
        result = self.db.execute_query(query, params)
        if result:
            return result[0]
        return None

    def find_by_id(self, user_id: int) -> Optional[User]:
        pass

    def delete(self, user_id: int) -> None:
        pass
