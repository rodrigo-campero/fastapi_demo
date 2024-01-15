from fastapi import FastAPI
from fastapi.responses import JSONResponse

from app.api.endpoints import bank
from app.core.config import settings
from app.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(bank.router)


@app.get("/")
def read_root():
    """
    Returns a dictionary with a message containing the app name.

    Returns:
        dict: A dictionary with a message containing the app name.
    """
    return {"message": f"Hello from {settings.app_name}"}


@app.exception_handler(404)
async def not_found_error_handler(request, exc):
    """
    Error handler for handling 404 Not Found errors.

    Args:
        request: The request object.
        exc: The exception object.

    Returns:
        A JSONResponse with a 404 status code and a message indicating "Not Found".
    """
    return JSONResponse(
        status_code=404,
        content={"message": "Not Found"},
    )
