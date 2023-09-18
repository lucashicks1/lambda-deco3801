from fastapi import Body, APIRouter, HTTPException
from app.dependencies.database import cal_col, user_col
import time as time_lib
import app.utils as utils
from typing import Annotated

router = APIRouter(
    prefix="/whiteboard",
    tags=["Whiteboard"]
)


@router.post("/{user}")
def modify_calendar(user: str, payload: Annotated[dict, Body(
    examples=[
        {
            "body": [
                {
                    "day": "Monday",
                    "time_slot": 0,
                    "data": "captured text"
                },
                {
                    "day": "Tuesday",
                    "time_slot": 0,
                    "data": "text"
                }
            ]
        }
    ]
)]):
    users = user_col.distinct("user_id")
    users.append("family")
    if user not in users:
        raise HTTPException(status_code=400, detail="That user_id is not valid")
    for calendar_slot in payload.get("body"):
        print(calendar_slot)
    return {"message": user}


