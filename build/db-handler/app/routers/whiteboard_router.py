"""Router for whiteboard endpoints"""
import logging
from typing import Annotated
from fastapi import Body, APIRouter, HTTPException
from app.dependencies.database import cal_col, user_col
from app.models.whiteboard_models import WhiteboardRequest
from app.examples.whiteboard_payloads import (
    POST_WHITEBOARD,
    RESPONSE_WHITEBOARD,
)
from app.constants import LOGGER_FORMAT, LOGGER_TIME_FORMAT
from app import utils

router = APIRouter(prefix="/whiteboard", tags=["Whiteboard"])

logging.basicConfig(level=logging.INFO, format=LOGGER_FORMAT, datefmt=LOGGER_TIME_FORMAT)
_LOGGER = logging.getLogger(__name__)
logging.getLogger(__name__).setLevel(logging.DEBUG)


@router.post("/{user}")
def modify_calendar(
    user: str,
    payload: Annotated[WhiteboardRequest, Body(examples=[POST_WHITEBOARD])],
) -> Annotated[dict, Body(examples=[RESPONSE_WHITEBOARD])]:
    """Endpoint that updates the calendar with information given to the image capture software.

    Raises:
        HTTPException: 400 status code if the user provided is not valid

    Returns:
        dict: added timeslots
    """
    # Check if the user name given in the path is in the database
    # If not, return a status code of 400 - bad request
    users = user_col.distinct("user_id")
    if user not in users:
        _LOGGER.error("User not found in database, bad request")
        raise HTTPException(status_code=400, detail="That user_id is not valid")

    _LOGGER.info("User found in database, proceeding to update")

    # Deletes the user from the db timeslots
    cal_col.update_many({}, {"$pull": {"booked_users": user}})

    # Goes through each payload and updates the database
    for time_slot in payload.body:
        _LOGGER.debug(
            "Day: %s Slot_number: %d Time: %s, Data: %s Colour: %s",
            time_slot.day,
            time_slot.time_slot,
            utils.timeslot_num_to_time(time_slot.time_slot),
            time_slot.data,
            time_slot.colour.split(",")
        )
        cal_col.update_one(filter,
            {
                "day": time_slot.day,
                "slot_num": time_slot.time_slot
            },
            {
                "$push": {
                    "booked_users": user
                },
                "$set": {
                    "data": time_slot.data,
                    "colour": time_slot.colour.split(",")
                }
            },
        )

    return {"body": list(cal_col.find({"booked_users": {"$in": [user]}}, {"_id": 0}))}
