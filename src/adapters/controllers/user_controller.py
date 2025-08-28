from infra.repositories.user_repository import UserRepository
from src.application.use_cases import UserUseCases
from domain.entities.user import User
from fastapi import APIRouter
from fastapi.responses import JSONResponse

user_router = APIRouter()

user_repository = UserRepository()
user_user_case = UserUseCases(user_repository)


@user_router.post("/users/")
async def create_user(user_data: User) -> JSONResponse:

    try:
        result = user_user_case.create_user(user_data)
        if not result:
            result = {}
        return JSONResponse(content=result, status_code=200)
    except ValueError as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
    except Exception as e:
        return JSONResponse(
            content={"error": "An unexpected error occurred: " + str(e)},
            status_code=500,
        )
