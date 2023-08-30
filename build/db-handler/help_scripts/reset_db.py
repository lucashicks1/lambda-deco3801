from app.dependencies.database import cal_col, user_col
import app.constants as constants

DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

cal_col.delete_many({})
user_col.delete_many({})

for day in DAYS:
    minute: int = 0
    hour: int = 0
    while hour < 24:
        cal_col.insert_one({
            "day": day,
            "time": f"{hour:02}:{minute:02}",
            "booked_users": []
        })
        minute += constants.TIMESLOT_LEN
        if minute == 60:
            minute = 0
            hour += 1

cal_col.update_many(filter={}, update={"$set": {"booked_users": [constants.USERS[0]]}})

for user in constants.USERS:
    user_col.insert_one({"user": user})

cursor = cal_col.find({})

for doc in cursor:
    print(doc)

cursor = user_col.find({})

for doc in cursor:
    print(doc)