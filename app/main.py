from fastapi import FastAPI
from .routers import item
from .database import app

app.include_router(item.router, prefix="/items", tags=["items"])
