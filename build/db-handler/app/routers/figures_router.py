"""Router for figurine endpoints"""
import time as time_lib
from typing import Annotated
from fastapi import Body, APIRouter
from app.dependencies.database import cal_col, user_col
from app import utils
from app.examples.figurines_payloads import FIGURINES_EXAMPLE

router = APIRouter(prefix='/figurines', tags=['Figurines'])


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
    timeslot: str = utils.current_to_timeslot()
    # Finds the timeslot in the database at the current time
    booked_users = cal_col.find_one(
        {'day': time_lib.strftime('%A').lower(), 'time': timeslot}
    ).get('booked_users')

    # Populates dictionary. 1 if user is booked, 0 is free
    for user in user_col.distinct('user_id'):
        status = 1 if user in booked_users else 0
        users[user] = status
    return users
