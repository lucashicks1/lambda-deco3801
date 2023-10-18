"""Utils file for basic utility functions used throughout the database handler"""
from datetime import datetime
import random
from app import constants
from app.dependencies import database as db


def current_to_timeslot() -> str:
    """Calculates the current timeslot to a string that is used in the database

    Returns:
        str: string representation of the current timeslot
    """
    now = datetime.now()
    # Gets current time with minutes rounded down to the closest 15 minute timeslot
    return f'{now.hour:02}:{now.minute // constants.TIMESLOT_LEN * constants.TIMESLOT_LEN:02}'


def timeslot_num_to_time(slot_num: int) -> str:
    """Calculates the time for a given timeslot number

    Returns:
        str: str representation of the time for that timeslot
    """
    hour: str = slot_num // (60 // constants.TIMESLOT_LEN) + constants.START_HOUR
    minute: str = (slot_num % (60 // constants.TIMESLOT_LEN)) * constants.TIMESLOT_LEN
    return f"{hour:02}:{minute:02}"


def reset_db(populate: bool = False):
    """Resets the database and adds in random timeslot information"""
    db.cal_col.delete_many({})
    db.user_col.delete_many({})

    # Adds users
    for user in constants.USERS:
        db.user_col.insert_one({'user_id': user})

    # Go through the hours betwen the start hour until the hour just before the end hour
    # Create the documents in the collection

    for day in constants.DAYS:
        timeslot_num: int = 0
        for hour in range(constants.START_HOUR, constants.END_HOUR):
            for minute in range(60 // constants.TIMESLOT_LEN):
                users = random.sample(constants.USERS, random.randint(0, len(constants.USERS))) if populate else []
                document = {
                    'day': day,
                    'time': f'{hour:02}:{(minute * constants.TIMESLOT_LEN):02}',
                    'slot_num': timeslot_num,
                    'booked_users': users
                }
                db.cal_col.insert_one(document)
                timeslot_num += 1
        minute = 0
        # Adds the last hour of the calendar as a document
        while minute <= constants.END_MINUTE:
            document = {
                'day': day,
                'time': f'{constants.END_HOUR:02}:{minute:02}',
                'slot_num': timeslot_num,
                'booked_users': []
            }
            db.cal_col.insert_one(document)
            minute += constants.TIMESLOT_LEN
            timeslot_num += 1
