from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Configuration settings for the FastAPI app.
    """

    app_name: str = "My FastAPI App"
    debug: bool = False
    database_url: str = "sqlite:///./test.db"

    class Config:
        """
        Configuration class for handling environment variables.
        """

        env_file = "env"


settings = Settings()
