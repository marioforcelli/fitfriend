from src.adapters.schemas.user import UserCreateSchema, FinalUserResponseSchema, UserResponseSchema
from src.adapters.providers.user import UserProvider
from src.infra.repositories.user_repository import UserRepository
from src.application.use_cases import UserUseCases
from src.domain.entities.user import User
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse

user_router = APIRouter()
user_repository = UserRepository()


@user_router.post("/users", response_model=FinalUserResponseSchema)
async def create_user(user_data: UserCreateSchema, use_case: UserUseCases = Depends(UserProvider())) -> FinalUserResponseSchema:

    try:
        user_entity = User(
            full_name=user_data.full_name,
            email=user_data.email,
            weight=user_data.weight,
            height=user_data.height,
            birth_date=user_data.birth_date
        )
        result = use_case.create_user(user_entity)
        user_response = FinalUserResponseSchema(
            success=True,
            data=UserResponseSchema(**vars(result))
        )
        return user_response
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred: " + str(e) )
