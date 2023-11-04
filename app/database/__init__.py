from motor.motor_asyncio import AsyncIOMotorClient
from fastapi import FastAPI
from contextlib import asynccontextmanager
import os


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.mongodb_client = AsyncIOMotorClient(os.environ.get("MONGODB_URL"))
    app.mongodb = app.mongodb_client["shayari_dev"]
    try:
        await app.mongodb_client.admin.command("ping")
        print("[+] Pinged the deployment successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    yield
    app.mongodb_client.close()
    print("[+] Closed to database successfully.")


async def get_database():
    return app.mongodb


app = FastAPI(lifespan=lifespan)
