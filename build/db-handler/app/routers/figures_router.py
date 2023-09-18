from fastapi import Body, APIRouter
from app.dependencies.database import cal_col, user_col
import time as time_lib
import app.utils as utils
from typing import Annotated
from app import constants
from app.examples.figurines_payloads import FIGURINES_EXAMPLE

router = APIRouter(
    prefix="/figurines",
    tags=["Figurines"]
)


@router.get("", summary="Gets map of all users and their availability for that timeslot. 1 represents busy, 0 represents free")
async def get_available() -> Annotated[dict, Body(examples=[FIGURINES_EXAMPLE])]:
    users: dict = {}
    timeslot: str = utils.current_to_timeslot()
    booked_users = cal_col.find_one({"day": time_lib.strftime("%A").lower(), "time": timeslot}).get("booked_users")
    for user in user_col.distinct("user_id", {"user_id": {"$ne": constants.FAMILY_NAME}}):
        status = 1 if user in booked_users else 0
        users[user] = status
    return users
