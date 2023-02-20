from app.api.api_v1.router.user.endpoints import login
from fastapi import APIRouter

router = APIRouter()
# router.include_router(login.router, tags=["login"])

