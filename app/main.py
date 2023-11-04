from .routers import item
from .database import app
from dotenv import load_dotenv, find_dotenv

# For Production
load_dotenv(find_dotenv())
# For Dev Server
# load_dotenv(find_dotenv(".env.dev"))

app.include_router(item.router, prefix="/items", tags=["items"])
