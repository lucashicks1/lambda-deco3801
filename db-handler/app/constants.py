"""App constants"""
TIMESLOT_LEN = 30

# Calendar hours and minute ends and starts for making timeslots
START_HOUR = 5
START_MINUTE = 0
END_HOUR = 22
END_MINUTE = 0

DAYS = [
    'monday',
    'tuesday',
    'wednesday',
    'thursday',
    'friday',
    'saturday',
    'sunday',
]

# Family and user names
FAMILY_NAME = 'family'
USERS = ['Timmy', 'Jimmy', 'Kimmy', 'Timmy_Jr', FAMILY_NAME]

LOGGER_FORMAT = "%(asctime)s %(levelname)s %(message)s"
LOGGER_TIME_FORMAT = '%I:%M:%S %p'

# Values for microcontroller and servos/actuators
FREE = 1  # 0 is sent to the microcontroller if user is not busy
BUSY = 0  # 1 is sent to the microcontroller if user is busy
