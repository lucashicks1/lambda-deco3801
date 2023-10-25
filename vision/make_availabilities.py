import json
import os


users = {
    'Timmy': [],
    'Kimmy': [],
    'Jimmy': [],
    'Timmy_Jr': [],
}
timmy_time_slots = {
    'monday': [0, 1, 2, 3, 4, 5, 6, 7],
    'tuesday': [0, 1, 2, 3, 4, 5, 6, 7],
    'wednesday': [0, 1, 2, 3, 4, 5, 6, 7],
    'thursday': [0, 1, 2, 3, 4, 5, 6, 7],
    'friday': [0, 1, 2, 3, 4, 5, 6, 7],
    'saturday': [0, 1, 2, 3, 4, 5, 6, 7],
    'sunday': [0, 1, 2, 3, 4, 5, 6, 7],
}
timmj_time_slots = {
    'monday': [0, 1, 2, 3, 4, 5, 6, 7],
    'tuesday': [0, 1, 2, 3, 4, 5, 6, 7],
    'wednesday': [0, 1, 2, 3, 4, 5, 6, 7],
    'thursday': [0, 1, 2, 3, 4, 5, 6, 7],
    'friday': [0, 1, 2, 3, 4, 5, 6, 7],
    'saturday': [0, 1, 2, 3, 4, 5, 6, 7],
    'sunday': [0, 1, 2, 3, 4, 5, 6, 7],
}
jimmy_time_slots = {
    'monday': [0, 1, 2, 3, 4, 5, 6, 7],
    'tuesday': [0, 1, 2, 3, 4, 5, 6, 7],
    'wednesday': [0, 1, 2, 3, 4, 5, 6, 7],
    'thursday': [0, 1, 2, 3, 4, 5, 6, 7],
    'friday': [0, 1, 2, 3, 4, 5, 6, 7],
    'saturday': [0, 1, 2, 3, 4, 5, 6, 7],
    'sunday': [0, 1, 2, 3, 4, 5, 6, 7],
}
kimmy_time_slots = {
    'monday': [0, 1, 2, 3, 4, 5, 6, 7],
    'tuesday': [0, 1, 2, 3, 4, 5, 6, 7],
    'wednesday': [0, 1, 2, 3, 4, 5, 6, 7],
    'thursday': [0, 1, 2, 3, 4, 5, 6, 7],
    'friday': [0, 1, 2, 3, 4, 5, 6, 7],
    'saturday': [0, 1, 2, 3, 4, 5, 6, 7],
    'sunday': [0, 1, 2, 3, 4, 5, 6, 7],
}


def make_json(person):
    result = []
    for day in person:
        for time in day:
            result.append(
                {'day': day, 'time_slot': time, 'data': '', 'colour': 'black'}
            )

    return result


for time_slots in make_json(timmy_time_slots):
    users.get('Timmy').append(time_slots)

for time_slots in make_json(timmj_time_slots):
    users.get('Timmy_Jr').append(time_slots)

for time_slots in make_json(kimmy_time_slots):
    users.get('Kimmy').append(time_slots)

for time_slots in make_json(jimmy_time_slots):
    users.get('Jimmy').append(time_slots)


for user in users:
    path = os.path.abspath(f'./premade/{user}.json')
    print(path)
    with open(path, 'w') as file:
        json.dump(users.get(user), file, indent=4)
