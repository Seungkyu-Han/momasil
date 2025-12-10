from contextlib import asynccontextmanager
from fastapi import FastAPI

from database.check_db_connection import check_db_connection


@asynccontextmanager
async def lifespan(app: FastAPI):
    await check_db_connection()
    yield