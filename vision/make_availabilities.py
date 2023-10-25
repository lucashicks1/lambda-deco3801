import json
import os


users = {
    'Timmy': [],
    'Kimmy': [],
    'Jimmy': [],
    'Timmy_Jr': [],
}
timmy_time_slots = {
    'monday': [8, 9, 10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25],
    'tuesday': [8, 9, 10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25, 28, 29, 30, 31, 32, 33],
    'wednesday': [8, 9, 10, 11, 12, 13, 14, 15, 18],
    'thursday': [8, 9, 10, 11, 12, 13, 14, 15],
    'friday': [8, 9, 10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24, 25],
    'saturday': [12, 13, 14, 15],
}
timmj_time_slots = {
    'monday': [24, 25, 26, 27, 28, 29],
    'wednesday': [22, 23, 24, 25, 26],
    'thursday': [24, 25, 26, 27, 28, 29, 30, 31, 32, 33],
    'saturday': [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33],
    'sunday': [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33],
}
jimmy_time_slots = {
    'monday': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 16, 17, 18, 19, 20, 21, 22],
    'tuesday': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 16, 17, 18, 19],
    'wednesday': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 19, 20, 21, 24, 25, 26, 27, 28],
    'thursday': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    'friday': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 15, 16, 17, 18, 19],
    'saturday': [18, 19, 20, 21, 22, 23, 24, 25, 26, 27],
    'sunday': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
}
kimmy_time_slots = {
    'monday': [10, 11, 12, 13, 15, 16, 17, 18, 27, 30, 31, 32, 33],
    'tuesday': [16, 24, 25, 26, 27],
    'wednesday': [16, 17, 20, 21, 22, 23],
    'thursday': [16, 17, 18, 19, 20, 21, 22, 23, 24],
    'friday': [18, 19, 20, 21, 22, 23, 24, 25, 26, 27],
    'saturday': [0, 1, 2, 3, 4, 5, 14, 15, 16],
    'sunday': [16, 17, 18, 19],
}


def make_json(person):
    result = []
    for day in person:
        for time in person.get(day):
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
