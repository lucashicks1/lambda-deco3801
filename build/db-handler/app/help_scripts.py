from app.dependencies.database import cal_col, user_col
import app.constants as constants
import random


def reset_db():
    cal_col.delete_many({})
    user_col.delete_many({})

    # Adds users
    for user in constants.USERS:
        user_col.insert_one({'user_id': user})

    # Adds timeslots
    for day in constants.DAYS:
        minute: int = 0
        hour: int = 0
        timeslot_num: int = 0
        while hour < 24:
            document = {
                'day': day,
                'time': f'{hour:02}:{minute:02}',
                'slot_num': timeslot_num,
                'booked_users': random.sample(
                    constants.USERS, random.randint(0, len(constants.USERS))
                ),
            }
            cal_col.insert_one(document)
            minute += constants.TIMESLOT_LEN
            if minute == 60:
                minute = 0
                hour += 1
            timeslot_num += 1

    print('\nTIMESLOTS')
    cursor = cal_col.find({})
    for doc in cursor:
        print(doc)

    print('\nUSERS')
    cursor = user_col.find({})
    for doc in cursor:
        print(doc)
