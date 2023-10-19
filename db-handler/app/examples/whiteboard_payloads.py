"""Payloads for whiteboard endpoints"""
POST_WHITEBOARD = {
    'body': [
        {
            'day': 'monday',
            'time_slot': 0,
            'data': 'captured text',
            'colour': 'black',
        },
        {
            'day': 'tuesday',
            'time_slot': 0,
            'data': 'text',
            'colour': 'black,red',
        },
    ]
}

RESPONSE_WHITEBOARD = {
    'body': [
        {
            'day': 'monday',
            'time': '00:00',
            'slot_num': 0,
            'booked_users': ['user_2', 'user_3', 'user_1'],
        },
        {
            'day': 'tuesday',
            'time': '00:00',
            'slot_num': 0,
            'booked_users': ['user_1'],
        },
    ]
}
