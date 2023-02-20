from app.api.api_v1.router import home
from app.api.api_v1.router.user import endpoints
from fastapi import APIRouter

api_v1_router = APIRouter()
api_v1_router.include_router(endpoints.router)
api_v1_router.include_router(home.router, tags=["首页"])


