from src.adapters.schemas.user import UserCreateSchema, UserResponseSchema
from src.adapters.schemas.base_schema import ResponseSchema
from src.adapters.providers.user import UserProvider
from src.application.use_cases import UserUseCases
from src.domain.entities.user import User
from fastapi import APIRouter, Depends, HTTPException

user_router = APIRouter()


@user_router.post("/users", response_model=ResponseSchema[UserResponseSchema])
async def create_user(
    user_data: UserCreateSchema, use_case: UserUseCases = Depends(UserProvider())
) -> ResponseSchema[UserResponseSchema]:

    try:
        user_entity = User(
            full_name=user_data.full_name,
            email=user_data.email,
            weight=user_data.weight,
            height=user_data.height,
            birth_date=user_data.birth_date,
        )
        result = use_case.create_user(user_entity)
        user_response: ResponseSchema[UserResponseSchema] = ResponseSchema(
            success=True, data=UserResponseSchema(**vars(result))
        )
        print(user_response)
        return user_response
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="An unexpected error occurred: " + str(e)
        )
