import json
from collections import namedtuple

import matplotlib.pyplot as plt
import numpy as np
import pytesseract
from PIL import Image
from tqdm import tqdm

days_of_the_week = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday',
}

Point = namedtuple('Point', ['X', 'Y'])
TimeSlot = namedtuple('TimeSlot', ['top_left', 'bottom_right'])

time_slot_width = 141
time_slot_height = 49
time_slot_size = time_slot_width * time_slot_height
num_time_slots = 35
num_days = 7


def main(image: Image):
    threshold = 100

    day_time_slots = [  # yay list comprehension :)
        TimeSlot(
            top_left=Point(time_slot_width * i, 0),
            bottom_right=Point(time_slot_width * (i + 1), time_slot_height),
        )
        for i in range(num_days)
    ]
    day_time_crops = []
    coloured_time_slots = []

    for day, (top_left, bottom_right) in enumerate(day_time_slots):
        time_crops = []
        print(f'On day {day}')
        for time_slot in tqdm(range(0, num_time_slots)):
            time_slot_crop = image.crop(
                (
                    top_left.X,
                    top_left.Y + time_slot * time_slot_height,
                    bottom_right.X,
                    bottom_right.Y + time_slot * time_slot_height,
                )
            )
            time_slot_array = np.array(time_slot_crop)
            threshold_mask = (time_slot_array <= threshold).all(axis=-1)
            num_coloured = np.sum(threshold_mask)
            is_coloured = (num_coloured / time_slot_size) * 100 >= 3
            time_crops.append((time_slot_crop, is_coloured))
            if is_coloured:
                ocr_result = pytesseract.image_to_string(time_slot_crop)
                coloured_time_slots.append(
                    {
                        'day': days_of_the_week.get(day),
                        'time_slot': time_slot,
                        'data': ocr_result,
                    }
                )
        day_time_crops.append(time_crops)
    fig, axes = plt.subplots(num_time_slots, num_days, figsize=(8, 12))
    axis_index = 0
    print('Mon\tTue\tWed\tThu\tFri\tSat\tSun')
    for time in range(5):
        print(
            f'{day_time_crops[0][time][1]}\t{day_time_crops[1][time][1]}\t'
            + f'{day_time_crops[2][time][1]}\t{day_time_crops[3][time][1]}\t'
            + f'{day_time_crops[4][time][1]}\t{day_time_crops[5][time][1]}\t'
            + f'{day_time_crops[6][time][1]}'
        )
    for i in range(num_time_slots):
        for j in range(num_days):
            axes.flat[axis_index].imshow(day_time_crops[j][i][0])
            axes.flat[axis_index].axis('off')
            axis_index += 1
    plt.tight_layout()
    plt.show()
    with open('coloured_time_slots.json', 'w') as json_file:
        json.dump(coloured_time_slots, json_file, indent=4)


def normalise_image(img_path: str) -> Image:
    """
    normalise_image()
    -----------------
    method for normalising our input image.
    """
    img = Image.open(img_path)

    left = 1013
    top = 219
    bottom = 1940
    right = 1990

    img = img.crop((left, top, right, bottom))
    img_array = np.array(img)
    threshold = 150

    white_mask = (img_array >= threshold).all(axis=-1)
    img_array[white_mask] = [255, 255, 255]
    img_array[~white_mask] = [0, 0, 0]
    new_img = Image.fromarray(img_array)

    return new_img


if __name__ == '__main__':
    path = './images/test1.jpg'
    image = normalise_image(path)
    # plt.imshow(image)
    # plt.show()
    main(image)
