import os
from dotenv import load_dotenv

load_dotenv()

def require_env(name: str) -> str:
    value = os.getenv(name)
    if value is None or value.strip() == "":
        raise EnvironmentError(f"env {name} is required")
    return value


def database_url() -> str:
    db_engine: str = os.getenv("DB_ENGINE", "postgresql+asyncpg")
    db_user: str = require_env("DB_USER")
    db_password: str = require_env("DB_PASSWORD")
    db_host: str = require_env("DB_HOST")
    db_port: str = require_env("DB_PORT")
    db_name: str = require_env("DB_NAME")

    return f"{db_engine}://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"