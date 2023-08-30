from fastapi import APIRouter
from app.dependencies.database import cal_col, user_col
from datetime import datetime
import time as time_lib
import app.constants as constants
import app.utils as utils

router = APIRouter(
    prefix="/figurines",
    tags=["figurines"]
)


@router.get("")
async def get_available():
    print(utils.current_to_timeslot_num())
    users: dict = {}
    day: str = time_lib.strftime("%A").lower()
    timeslot: str = utils.current_to_timeslot()
    booked_users = cal_col.find_one({"day": day, "time": timeslot}).get("booked_users")
    for user in user_col.distinct("user"):
        status = 0 if user in booked_users else 1
        users[user] = status
    return users
