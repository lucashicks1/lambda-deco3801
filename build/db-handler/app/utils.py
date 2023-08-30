from datetime import datetime
import time as time_lib
import app.constants as constants


def current_to_timeslot() -> str:
    now = datetime.now()
    # Gets current time with minutes rounded down to the closest 15 minute timeslot
    return f"{now.hour:02}:{now.minute // constants.TIMESLOT_LEN * constants.TIMESLOT_LEN:02}"


def current_to_timeslot_num() -> int:
    now = datetime.now()
    hour_slot: int = now.hour * 60 / constants.TIMESLOT_LEN
    minute_slot: int = (now.minute // constants.TIMESLOT_LEN * constants.TIMESLOT_LEN) / constants.TIMESLOT_LEN
    return hour_slot + minute_slot
