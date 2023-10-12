import numpy as np

days_of_the_week = {
    0: 'monday',
    1: 'tuesday',
    2: 'wednesday',
    3: 'thursday',
    4: 'friday',
    5: 'saturday',
    6: 'sunday',
}

time_slots = {
    0: '0500',
    1: '0530',
    2: '0600',
    3: '0630',
    4: '0700',
    5: '0730',
    6: '0800',
    7: '0830',
    8: '0900',
    9: '0930',
    10: '1000',
    11: '1030',
    12: '1100',
    13: '1130',
    14: '1200',
    15: '1230',
    16: '1300',
    17: '1330',
    18: '1400',
    19: '1430',
    20: '1500',
    21: '1530',
    22: '1600',
    23: '1630',
    24: '1700',
    25: '1730',
    26: '1800',
    27: '1830',
    28: '1900',
    29: '1930',
    30: '2000',
    31: '2030',
    32: '2100',
    33: '2130',
    34: '2200',
}

colour_thresholds = {
    'red_min': np.array([100, 0, 0]),
    'red_max': np.array([255, 100, 100]),
    'blue_min': np.array([0, 0, 100]),
    'blue_max': np.array([100, 100, 255]),
    'black_min': np.array([0, 0, 0]),
    'black_max': np.array([75, 75, 75]),
}

num_time_slots = 35
num_days = 7

python_path = '/Users/alexviller/micromamba/envs/tmp/bin/python'
