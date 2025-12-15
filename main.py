from fastapi import FastAPI

from cafe import cafe_router
from lifespan import lifespan

app = FastAPI(
    lifespan=lifespan,
    title="momasil",
)

app.include_router(cafe_router)

