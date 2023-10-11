import json
import sys
import time
from collections import namedtuple

import numpy as np
import pytesseract
from camera_constants import left
from camera_constants import time_slot_height
from camera_constants import time_slot_width
from camera_constants import top
from constants import colour_thresholds
from constants import days_of_the_week
from constants import num_days
from constants import num_time_slots
from constants import time_slots
from PIL import Image

Point = namedtuple('Point', ['X', 'Y'])
TimeSlot = namedtuple('TimeSlot', ['top_left', 'bottom_right'])


def main(image: Image):

    day_time_slots = [  # yay list comprehension :)
        TimeSlot(
            top_left=Point(time_slot_width * i, 0),
            bottom_right=Point(
                time_slot_width * (i + 1), np.floor(time_slot_height)
            ),
        )
        for i in range(num_days)
    ]
    coloured_time_slots = []

    for day, (top_left, bottom_right) in enumerate(day_time_slots):
        for time_slot in range(0, num_time_slots):
            time_slot_crop = image.crop(
                (
                    top_left.X,
                    np.floor(top_left.Y + time_slot * time_slot_height),
                    bottom_right.X,
                    np.floor(bottom_right.Y + time_slot * time_slot_height),
                )
            )
            time_slot_size = time_slot_crop.size[0] * time_slot_crop.size[1]
            time_slot_array = np.array(time_slot_crop)

            red_mask = np.all(
                (time_slot_array >= colour_thresholds.get('red_min'))
                & (time_slot_array <= colour_thresholds.get('red_max')),
                axis=-1,
            )
            blue_mask = np.all(
                (time_slot_array >= colour_thresholds.get('blue_min'))
                & (time_slot_array <= colour_thresholds.get('blue_max')),
                axis=-1,
            )
            black_mask = np.all(
                (time_slot_array >= colour_thresholds.get('black_min'))
                & (time_slot_array <= colour_thresholds.get('black_max')),
                axis=-1,
            )

            output_red = np.ones_like(time_slot_array) * 255
            output_blue = np.ones_like(time_slot_array) * 255
            output_black = np.ones_like(time_slot_array) * 255

            output_red[red_mask] = [0, 0, 0]
            output_blue[blue_mask] = [0, 0, 0]
            output_black[black_mask] = [0, 0, 0]

            num_coloured_red = np.count_nonzero(red_mask)
            num_coloured_blue = np.count_nonzero(blue_mask)
            num_coloured_black = np.count_nonzero(black_mask)

            pcent_red = (num_coloured_red / time_slot_size) * 100
            pcent_blue = (num_coloured_blue / time_slot_size) * 100
            pcent_black = (num_coloured_black / time_slot_size) * 100

            if pcent_blue >= 2:
                ocr_result = pytesseract.image_to_string(output_blue)
                coloured_time_slots.append(
                    {
                        'day': days_of_the_week.get(day),
                        'time_slot': time_slots.get(time_slot),
                        'colour': 'blue',
                        'data': ocr_result,
                    }
                )
            if pcent_red >= 2:
                ocr_result = pytesseract.image_to_string(output_red)
                coloured_time_slots.append(
                    {
                        'day': days_of_the_week.get(day),
                        'time_slot': time_slots.get(time_slot),
                        'colour': 'red',
                        'data': ocr_result,
                    }
                )
            if pcent_black >= 18:
                ocr_result = pytesseract.image_to_string(output_black)
                coloured_time_slots.append(
                    {
                        'day': days_of_the_week.get(day),
                        'time_slot': time_slots.get(time_slot),
                        'colour': 'black',
                        'data': ocr_result,
                    }
                )

    with open('coloured_time_slots.json', 'w') as json_file:
        json.dump(coloured_time_slots, json_file, indent=4)


def crop_image(img_path: str) -> Image:
    """
    normalise_image()
    -----------------
    method for cropping our input image to the top left corner of the calendar.
    """
    try:
        img = Image.open(img_path)
        img = img.crop((left, top, img.size[0], img.size[1]))
        return img.convert('RGB')
    except Exception as e:
        print(f"Error: {e} has occurred.")
        print(f"Check path: {img_path}")
        exit()


if __name__ == '__main__':
    start = time.time()
    path = sys.path[0] + '/'
    if len(sys.argv) > 1:
        if sys.argv[1][0] == '/':
            path = sys.argv[1]
        else:
            path = sys.argv[1]
    else:
        path += 'images/test-mix.jpg'
    image = crop_image(path)
    main(image)
    print(f'took {time.time() - start}')
