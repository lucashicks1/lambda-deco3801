USER_TOTALS_EXAMPLES = {
    "user_1": 81.5,
    "user_2": 85.25,
    "user_3": 84.75,
    "user_4": 79
}

FAMILY_TIMESLOTS_EXAMPLE = {
    "body": [
        {
            "day": "monday",
            "time": "14:00",
            "slot_num": 56,
            "booked_users": [
                "family",
                "user_2"
            ]
        },
        {
            "day": "monday",
            "time": "14:15",
            "slot_num": 57,
            "booked_users": [
                "family"
            ]
        },
        {
            "day": "monday",
            "time": "14:30",
            "slot_num": 58,
            "booked_users": [
                "family"
            ]
        },
        {
            "day": "monday",
            "time": "14:45",
            "slot_num": 59,
            "booked_users": [
                "family"
            ]
        },
        {
            "day": "tuesday",
            "time": "15:00",
            "slot_num": 60,
            "booked_users": [
                "family",
                "user_2"
            ]
        }
    ]
}

FREE_TIMESLOTS_EXAMPLE = {
    "body": [
        {
            "day": "monday",
            "time": "08:00",
            "slot_num": 32,
            "booked_users": [],
            "num_free_users": 4
        },
        {
            "day": "monday",
            "time": "08:15",
            "slot_num": 33,
            "booked_users": [],
            "num_free_users": 4
        },
        {
            "day": "monday",
            "time": "08:30",
            "slot_num": 34,
            "booked_users": [],
            "num_free_users": 4
        },
        {
            "day": "tuesday",
            "time": "14:30",
            "slot_num": 58,
            "booked_users": ["user_1"],
            "num_free_users": 3
        },
        {
            "day": "tuesday",
            "time": "14:45",
            "slot_num": 59,
            "booked_users": ["user_1"],
            "num_free_users": 3
        },
    ]
}
