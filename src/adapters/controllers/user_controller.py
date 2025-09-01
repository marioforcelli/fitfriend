from src.domain.exceptions.user import UserAlreadyExistsError, UserNotFoundError
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
            birth_date=str(user_data.birth_date),
            phone=user_data.phone,
        )
        result = use_case.create_user(user_entity)
        user_response: ResponseSchema[UserResponseSchema] = ResponseSchema(
            success=True, data=UserResponseSchema(**vars(result))
        )
        print(user_response)
        return user_response
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except UserAlreadyExistsError as e:
        raise HTTPException(status_code=409, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="An unexpected error occurred: " + str(e)
        )


@user_router.get("/users", response_model=ResponseSchema[UserResponseSchema])
async def get_user(
    email: str, use_case: UserUseCases = Depends(UserProvider())
) -> ResponseSchema[UserResponseSchema] | None:

    try:
        print(email)
        user: User | None = use_case.get_user_by_email(email)

        if user:
            user_entity = User(
                full_name=user.full_name,
                email=user.email,
                weight=user.weight,
                height=user.height,
                birth_date=user.birth_date,
                phone=user.phone,
            )
            print(user_entity)
            return ResponseSchema(
                success=True, data=UserResponseSchema(**vars(user_entity))
            )

    except UserNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="An unexpected error occurred: " + str(e)
        )


@user_router.put("/users/{user_id}", response_model=ResponseSchema[UserResponseSchema])
async def update_user(
    user_id: int,
    user_data: UserCreateSchema,
    use_case: UserUseCases = Depends(UserProvider()),
) -> ResponseSchema[UserResponseSchema]:

    try:
        user_entity = User(
            id=user_id,
            full_name=user_data.full_name,
            email=user_data.email,
            weight=user_data.weight,
            height=user_data.height,
            birth_date=str(user_data.birth_date),
            phone=user_data.phone,
        )
        result = use_case.update_user(user_entity)
        user_response: ResponseSchema[UserResponseSchema] = ResponseSchema(
            success=True, data=UserResponseSchema(**vars(result))
        )
        print(user_response)
        return user_response
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except UserNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="An unexpected error occurred: " + str(e)
        )


@user_router.delete("/users/{user_id}", status_code=204)
async def delete_user(user_id: int, use_case: UserUseCases = Depends(UserProvider())):

    try:
        use_case.delete_user(user_id)
        return ResponseSchema(success=True, data=None)
    except UserNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(
            status_code=500, detail="An unexpected error occurred: " + str(e)
        )
