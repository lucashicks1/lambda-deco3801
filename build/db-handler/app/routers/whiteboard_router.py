from fastapi import Body, APIRouter, HTTPException
from app.dependencies.database import cal_col, user_col
from typing import Annotated, List, Dict
from app.models.whiteboard_models import WhiteboardRequest
from app.examples.whiteboard_payloads import POST_WHITEBOARD, RESPONSE_WHITEBOARD
from app import constants

router = APIRouter(
    prefix="/whiteboard",
    tags=["Whiteboard"]
)


@router.post("/{user}")
def modify_calendar(user: str, payload: Annotated[WhiteboardRequest, Body(examples=[POST_WHITEBOARD])]) -> Annotated[
    dict, Body(examples=[RESPONSE_WHITEBOARD])]:
    users = user_col.distinct("user_id")
    if user not in users:
        raise HTTPException(status_code=400, detail="That user_id is not valid")

    cal_col.update_many({}, {"$pull": {"booked_users": user}})

    for time_slot in payload.body:
        cal_col.update_one(
            {
                "day": time_slot.day,
                "slot_num": time_slot.time_slot
            },
            {
                "$push": {
                    "booked_users": user
                }
            }
        )

    return {"body": list(cal_col.find({"booked_users": {"$in": [user]}}, {"_id": 0}))}
