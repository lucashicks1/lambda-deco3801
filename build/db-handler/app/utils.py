from datetime import datetime
import time as time_lib
import app.constants as constants
import app.dependencies.database as db


def current_to_timeslot() -> str:
    now = datetime.now()
    # Gets current time with minutes rounded down to the closest 15 minute timeslot
    return f"{now.hour:02}:{now.minute // constants.TIMESLOT_LEN * constants.TIMESLOT_LEN:02}"


def current_to_timeslot_num() -> int:
    now = datetime.now()
    hour_slot: int = now.hour * 60 / constants.TIMESLOT_LEN
    minute_slot: int = (now.minute // constants.TIMESLOT_LEN * constants.TIMESLOT_LEN) / constants.TIMESLOT_LEN
    return hour_slot + minute_slot


def reset_db():
    db.cal_col.delete_many({})
    db.user_col.delete_many({})

    for day in constants.DAYS:
        minute: int = 0
        hour: int = 0
        timeslot_num: int = 0
        while hour < 24:
            document = {
                "day": day,
                "time": f"{hour:02}:{minute:02}",
                "slot_num": timeslot_num,
                "booked_users": []
            }
            db.cal_col.insert_one(document)
            minute += constants.TIMESLOT_LEN
            if minute == 60:
                minute = 0
                hour += 1
            timeslot_num += 1

    db.cal_col.update_many(filter={}, update={"$set": {"booked_users": [constants.USERS[0]]}})

    for user in constants.USERS:
        db.user_col.insert_one({"user_id": user})

    cursor = db.cal_col.find({})

    for doc in cursor:
        print(doc)

    cursor = db.user_col.find({})

    for doc in cursor:
        print(doc)
