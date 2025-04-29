from .routes import router
from fastapi import APIRouter

rout = APIRouter()
rout.include_router(router)