from fastapi import FastAPI

from cafe import cafe_router
from crawler import crawler_router
from menu import menu_router
from cart import cart_router
from lifespan import lifespan

app = FastAPI(
    lifespan=lifespan,
    title="momasil",
)

app.include_router(cafe_router)

app.include_router(menu_router)

app.include_router(crawler_router)

app.include_router(cart_router)