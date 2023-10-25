"""Router for figurine endpoints"""
import time as time_lib
import logging
from typing import Annotated
from fastapi import Body, APIRouter
from app.dependencies.database import cal_col, user_col
from app import utils
from app.examples.figurines_payloads import FIGURINES_EXAMPLE
from app.constants import LOGGER_FORMAT, LOGGER_TIME_FORMAT, BUSY, FREE, FAMILY_NAME

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
    # users: dict = {}
    time: tuple = utils.current_to_timeslot()
    timeslot_time: str = time[0]
    timeslot_time = "15:30"
    day: str = time[1]
    _LOGGER.info("Getting availability for %s, %s", day, timeslot_time)
    # Finds the timeslot in the database at the current time
    booked_timeslot = cal_col.find_one(
        {'day': time_lib.strftime('%A').lower(), 'time': timeslot_time}
    )

    # Populates dictionary. 1 if user is booked, 0 is free
    if booked_timeslot is None:
        _LOGGER.info("Current time is not shown on calendar")
        return {key: BUSY for key in user_col.distinct("user_id")}

    users: dict = {
        f"0{FAMILY_NAME}": FREE if FAMILY_NAME in booked_timeslot.get("booked_users") else BUSY,
        f"1Timmy": BUSY if "Timmy" in booked_timeslot.get("booked_users") else FREE,
        f"2Kimmy": BUSY if "Kimmy" in booked_timeslot.get("booked_users") else FREE,
        f"3Jimmy": BUSY if "Jimmy" in booked_timeslot.get("booked_users") else FREE,
        f"4Timmy_Jr": BUSY if "Timmy_Jr" in booked_timeslot.get("booked_users") else FREE
    }

    _LOGGER.debug("Sending dict: %s \n", users)
    return users
