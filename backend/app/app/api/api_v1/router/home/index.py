from fastapi import APIRouter

from app.api.utils.responseCode import resp_200

router = APIRouter()


async def action(
        limit: int = 8,
        page: int = 1,
        username: str = None,
        module_name: str = None,
        start_time: str = None,
        end_time: str = None
):
    return resp_200()


router.add_api_route(methods=['GET'], path="/",
                     endpoint=action, summary="action")
