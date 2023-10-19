import json
import sys
from collections import namedtuple

import numpy as np
import requests
import pytesseract
from camera_constants import left
from camera_constants import time_slot_height
from camera_constants import time_slot_width
from camera_constants import top
from constants import colour_thresholds
from constants import days_of_the_week
from constants import num_days
from constants import num_time_slots
from PIL import Image

Point = namedtuple('Point', ['X', 'Y'])
TimeSlot = namedtuple('TimeSlot', ['top_left', 'bottom_right'])

USER_NAME = "family"


def main(image: Image):
    """
    main()
    ------
    This is the main loop of the program. This handles almost all logic.

    :param image: The image to be processed
    """
    day_time_slots = [
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
            time_slot_array = np.array(time_slot_crop)
            is_coloured, colour, ocr_result = get_info(time_slot_array)

            if is_coloured:
                coloured_time_slots.append(
                    {
                        'day': days_of_the_week.get(day),
                        'time_slot': time_slot,
                        'data': ocr_result,
                        'colour': ','.join(colour),  # logic to get out of list
                    }
                )
    
    request_body = {"body": coloured_time_slots}
    try:
        requests.post(f"http://127.0.0.1:8000/whiteboard/{USER_NAME}", json=request_body, timeout=30)
        with open('coloured_time_slots.json', 'w') as json_file:
            json.dump(coloured_time_slots, json_file, indent=4)
    except requests.exceptions.ConnectionError as e:
        print(f"Error making HTTP request - {e}")



def get_info(time_slot_array: np.ndarray) -> (bool, [str], str):
    """
    get_info()
    ----------
    Gets the information out of a time slot array.

    :param time_slot_array: the array created from converting an image to array.
    :return: a tuple containing boolean value for if the time slot is coloured,
             a list containing strings of the colours that it is coloured with,
             the string containing ocr result if applicable
    """
    time_slot_size = time_slot_array.shape[0] * time_slot_array.shape[1]

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

    # setting non coloured pixels all to white
    output_red = np.ones_like(time_slot_array) * 255
    output_blue = np.ones_like(time_slot_array) * 255
    output_black = np.ones_like(time_slot_array) * 255

    # setting coloured pixels all to black
    output_red[red_mask] = [0, 0, 0]
    output_blue[blue_mask] = [0, 0, 0]
    output_black[black_mask] = [0, 0, 0]

    # get the counts of the coloured pixels
    num_coloured_red = np.count_nonzero(red_mask)
    num_coloured_blue = np.count_nonzero(blue_mask)
    num_coloured_black = np.count_nonzero(black_mask)

    # find what percent they are of the whole image
    pcent_red = (num_coloured_red / time_slot_size) * 100
    pcent_blue = (num_coloured_blue / time_slot_size) * 100
    pcent_black = (num_coloured_black / time_slot_size) * 100

    # threshold this for how many pixels need to be coloured to think important
    is_blue = pcent_blue >= 2
    is_red = pcent_red >= 2
    is_black = pcent_black >= 20

    is_coloured = is_blue or is_red or is_black
    colour = []

    # add to the colour list
    if pcent_blue >= 2:
        colour.append('blue')
    if pcent_red >= 2:
        colour.append('red')
    if pcent_black >= 20:
        colour.append('black')

    ocr_result = pytesseract.image_to_string(output_black)

    return (is_coloured, colour, ocr_result)


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
        # Error for bad path
        print(f'Error: {e} has occurred.')
        print(f'Check path: {img_path}')
        exit()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        print('Please provide a path to an image')
        exit()
    image = crop_image(path)
    main(image)
