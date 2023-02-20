from fastapi import APIRouter

from app.api.utils.responseCode import resp_200

router = APIRouter()


def todos(
        limit: int = 8,
        page: int = 1,
        start_time: str = None,
        end_time: str = None
):
    return resp_200()


router.add_api_route(methods=['GET'], path="/", endpoint=todos, summary="todos")
