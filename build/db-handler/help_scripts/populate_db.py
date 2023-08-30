from app.dependencies.database import cal_col

TIMESLOT_INCREMENT = 15
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

for day in DAYS:
    minute: int = 0
    hour: int = 0
    while hour < 24:
        cal_col.insert_one({
            "day": day,
            "time": f"{hour:02}:{minute:02}",
            "booked_users": []
        })
        minute += 15
        if minute == 60:
            minute = 0
            hour += 1

cursor = cal_col.find({})

for doc in cursor:
    print(doc)