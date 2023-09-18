from fastapi import Body, APIRouter
from app.dependencies.database import cal_col, user_col
import time as time_lib
import app.utils as utils
from typing import Annotated

router = APIRouter(
    prefix="/figurines",
    tags=["Figurines"]
)


@router.get("", summary="Gets map of all users and their availability for that timeslot")
async def get_available() -> Annotated[dict, Body(
    examples=[
        {
            "user_1": 1,
            "user_2": 0,
            "user_3": 1
        }
    ]
)]:
    users: dict = {}
    timeslot: str = utils.current_to_timeslot()
    booked_users = cal_col.find_one({"day": time_lib.strftime("%A").lower(), "time": timeslot}).get("booked_users")
    for user in user_col.distinct("user_id"):
        status = 1 if user in booked_users else 0
        users[user] = status
    return users
