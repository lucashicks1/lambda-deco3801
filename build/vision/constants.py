import numpy as np

python_path = '/Users/alexviller/micromamba/envs/tmp/bin/python'


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

days_of_the_week = {
    0: 'monday',
    1: 'tuesday',
    2: 'wednesday',
    3: 'thursday',
    4: 'friday',
    5: 'saturday',
    6: 'sunday',
}
