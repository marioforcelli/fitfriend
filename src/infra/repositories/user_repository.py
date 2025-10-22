from src.domain.exceptions.user import UserAlreadyExistsError, UserNotFoundError
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
            query = "INSERT INTO users (full_name, email, birth_date, phone) VALUES (%s, %s, %s, %s) RETURNING id;"
            params = (
                user.full_name,
                user.email,
                user.birth_date,
                user.phone,
            )
            self.db.execute_query(query, params)
            return user
        except psycopg2.errors.UniqueViolation:
            print("Unique constraint violated")
            raise UserAlreadyExistsError("User with this email already exists.")

    def find_by_email(self, email: str) -> Optional[User]:
        try:
            print(email)
            query = "SELECT id, full_name, email, birth_date, phone FROM users WHERE email = %s;"
            params = (email,)
            print(query, params)
            result = self.db.fetch_one(query, params)
            print(result)
            if not result:
                return None
            return User(**result)
        except psycopg2.errors.NoDataFound:
            raise UserNotFoundError("User not found.")
        except Exception as e:
            print("Error occurred:", e)
            raise

    def find_by_id(self, user_id: int) -> Optional[User]:
        try:
            query = "SELECT full_name, email, birth_date, phone FROM users WHERE id = %s;"
            params = (user_id,)
            result = self.db.fetch_one(query, params)
            if not result:
                return None
            print({**result})
            return User(**result)
        except psycopg2.errors.NoDataFound:
            raise UserNotFoundError("User not found.")
        except Exception as e:
            print("Error occurred:", e)
            raise

    def delete(self, user_id: int) -> None:
        try:
            # Verificar se usuário existe antes de deletar
            existing_user = self.find_by_id(user_id)
            if existing_user is None:
                raise UserNotFoundError("User not found.")

            query = "DELETE FROM users WHERE id = %s;"
            params = (user_id,)

            # Usar execute_query que não espera retorno
            with self.db.connection.cursor() as cursor:
                cursor.execute(query, params)
                self.db.connection.commit()

        except UserNotFoundError:
            raise
        except Exception as e:
            print("Error occurred:", e)
            raise

    def update(self, user_data: User) -> User:
        try:
            if user_data.id is None:
                raise ValueError("User ID is required for update operation")

            # Verificar se usuário existe
            existing_user = self.find_by_id(user_data.id)
            if existing_user is None:
                raise UserNotFoundError("User not found.")

            query = """
                UPDATE users
                SET full_name = %s, email = %s, birth_date = %s, phone = %s
                WHERE id = %s
                RETURNING id;
            """
            params = (
                user_data.full_name,
                user_data.email,
                user_data.weight,
                user_data.height,
                user_data.birth_date,
                user_data.phone,
                user_data.id,
            )

            if user_data.id is not None and self.find_by_id(user_data.id) is None:
                raise UserNotFoundError("User not found.")
            self.db.execute_query(query, params)
            return user_data
        except psycopg2.errors.UniqueViolation:
            raise UserAlreadyExistsError("Email already exists for another user.")
        except psycopg2.errors.NoDataFound:
            raise UserNotFoundError("User not found.")
        except Exception as e:
            print("Error occurred:", e)
            raise
