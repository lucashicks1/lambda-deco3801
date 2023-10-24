import json
import os

from constants import days_of_the_week

users = ['Timmy', 'Kimmy', 'Jimmy', 'Timmy_Jr']
time_slots = [0, 1, 2, 3, 4, 5, 6, 7]
default = []

for day in days_of_the_week:
    for time_slot in time_slots:
        default.append(
            {'day': day, 'time_slot': time_slot, 'data': '', 'colour': 'black'}
        )

for user in users:
    path = os.path.abspath(f'./premade/{user}.json')
    print(path)
    with open(path, 'w') as file:
        json.dump(default, file, indent=4)
