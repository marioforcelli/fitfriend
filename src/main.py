import fastapi
from fastapi.responses import JSONResponse
from fastapi import HTTPException
from src.adapters.controllers.user_controller import user_router

app = fastapi.FastAPI()


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


@app.exception_handler(HTTPException)
async def http_exception_handler(request: fastapi.Request, exc: fastapi.HTTPException):
    success = False if exc.status_code != 200 else True
    return JSONResponse(
        status_code=exc.status_code, content={"success": success, "error": exc.detail}
    )


app.include_router(user_router, prefix="/api")
