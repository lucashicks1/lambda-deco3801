from app.dependencies.database import cal_col, user_col
import app.constants as constants
import random


def reset_db():
    cal_col.delete_many({})
    user_col.delete_many({})

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
            cal_col.insert_one(document)
            minute += constants.TIMESLOT_LEN
            if minute == 60:
                minute = 0
                hour += 1
            timeslot_num += 1

    cursor = cal_col.find({})
    for doc in cursor:
        cal_col.update_one(filter={"day": doc.get("day"), "time": doc.get("time")}, update={
            "$set": {"booked_users": [random.sample(constants.USERS, random.randint(0, len(constants.USERS)))]}})

    for user in constants.USERS:
        user_col.insert_one({"user_id": user})

    cursor = cal_col.find({})

    for doc in cursor:
        print(doc)

    cursor = user_col.find({})

    for doc in cursor:
        print(doc)
