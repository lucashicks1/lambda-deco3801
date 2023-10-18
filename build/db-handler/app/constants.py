"""App constants"""
TIMESLOT_LEN = 30

START_HOUR = 5
START_MINUTE = 0

END_HOUR = 22
END_MINUTE = 0

FAMILY_NAME = 'family'
USERS = ['user_1', 'user_2', 'user_3', 'user_4', FAMILY_NAME]
DAYS = [
    'monday',
    'tuesday',
    'wednesday',
    'thursday',
    'friday',
    'saturday',
    'sunday',
]
LOGGER_FORMAT = "%(asctime)s %(levelname)s %(message)s"
LOGGER_TIME_FORMAT = '%I:%M:%S %p'

# Values for microcontroller and servos/actuators
FREE = 0  # 0 is sent to the microcontroller if user is not busy
BUSY = 1  # 1 is sent to the microcontroller if user is busy
