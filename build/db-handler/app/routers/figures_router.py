"""Router for figurine endpoints"""
import time as time_lib
import logging
from typing import Annotated
from fastapi import Body, APIRouter
from app.dependencies.database import cal_col, user_col
from app import utils
from app.examples.figurines_payloads import FIGURINES_EXAMPLE
from app.constants import LOGGER_FORMAT, LOGGER_TIME_FORMAT

router = APIRouter(prefix='/figurines', tags=['Figurines'])



logging.basicConfig(level=logging.INFO, format=LOGGER_FORMAT, datefmt=LOGGER_TIME_FORMAT)
_LOGGER = logging.getLogger(__name__)
logging.getLogger(__name__).setLevel(logging.DEBUG)


@router.get(
    '',
    summary='Gets map of all users and their availability for that timeslot. 1 represents busy, '
    '0 represents free',
)
def get_available() -> Annotated[dict, Body(examples=[FIGURINES_EXAMPLE])]:
    """Endpoint that determines whether a user is free or not

    Returns:
        dict: map, mapping a user to their status
    """
    users: dict = {}
    timeslot_time: str = utils.current_to_timeslot()
    _LOGGER.info("Getting availability for %s", timeslot_time)
    # Finds the timeslot in the database at the current time
    booked_timeslot = cal_col.find_one(
        {'day': time_lib.strftime('%A').lower(), 'time': timeslot_time}
    )

    # Populates dictionary. 1 if user is booked, 0 is free
    if booked_timeslot is None:
        _LOGGER.info("Current time is not shown on calendar")
        return {key:0 for key in user_col.distinct("user_id")}
            
    _LOGGER.debug("Received timeslot back: %s", str(booked_timeslot))
    booked_users = booked_timeslot.get("booked_users")

    # Populates dictionary. 1 if user is booked, 0 is free
    return {user: 1 if user in booked_users else 0 for user in user_col.distinct("user_id")}

    # for user in user_col.distinct('user_id'):
    #     status = 1 if user in booked_users else 0
    #     users[user] = status
    # return users
