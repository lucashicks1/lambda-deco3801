import sys
from collections import namedtuple

import cv2
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from constants import num_days
from constants import num_time_slots
from PIL import Image

matplotlib.use('qtagg')

Point = namedtuple('Point', ['X', 'Y'])
TimeSlot = namedtuple('TimeSlot', ['top_left', 'bottom_right'])

"""
NOTE: This file contains lots of ensuring all windows are closed and pre set 
information for different libraries. This is due to an issue when importing
both open cv and matplotlib. These should fix all problems but may not work
on your machine.
"""


def get_rot_angle(path: str = 'cap.jpg') -> int:
    """
    get_rot_angle()
    ---------------
    method for prompting user to tell the orientation of their camera

    :param path: path to the image we are checking. Defaults to cap.jpg
    :return: the rotation angle
    """
    # default to 90 as calendar is portrait so makes sense
    angle = 90
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print('Error: Could not open camera')
        exit()

    cv2.namedWindow('Webcam', cv2.WINDOW_NORMAL)
    exit_flag = False

    while not exit_flag:
        ret, frame = cap.read()
        if not ret:
            print('Error: Could not read frame')
            break

        rows, cols, _ = frame.shape
        if angle == 0:
            rotated_frame = frame
        elif angle == 90:
            rotated_frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        elif angle == 180:
            rotated_frame = cv2.rotate(frame, cv2.ROTATE_180)
        elif angle == 270:
            rotated_frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)

        cv2.imshow('Webcam', rotated_frame)
        key = cv2.waitKey(1)

        if key == 27:  # wait for `esc` key to be pressed
            check = float(
                input('Please enter rotation angle, or -1 to exit: ')
            )
            exit_flag = check == -1
            if exit_flag:
                cv2.imwrite(path, rotated_frame)
            else:
                angle = check

    cv2.destroyAllWindows()
    cap.release()
    plt.close('all')
    return angle


def get_top_left(img: Image) -> (int, int):
    """
    get_top_left()
    --------------
    This method prompts user to find the top left corner of the information
    space of the calendar.

    :param img: The image that we are considering, after rotation.
    :return: a tuple of (left, top) which are the x, y coordinates of the
             corner
    """
    img_array = np.array(img)
    plt.imshow(img_array)
    plt.show(block=False)
    left = int(
        input(
            'Please enter the x value for the top left corner of the calendar: '
        )
    )
    top = int(
        input(
            'Please enter the y value for the top left corner of the calendar: '
        )
    )
    plt.close('all')
    return (left, top)


def show_crop(img: Image, top_left: (int, int)) -> bool:
    """
    show_crop()
    -----------
    This method shows the user a quick sanity check to ensure they are happy
    with their choice.

    :param img: the image we are considering.
    :param top_left: the coordinates they gave.
    :return: boolean based on if they are happy with their choice.
    """
    cropped = img.crop((top_left[0], top_left[1], img.size[0], img.size[1]))
    plt.imshow(cropped)
    plt.show(block=False)
    check = input('Is this a good crop? (y, [n]): ')

    plt.close('all')
    return check == 'y'


def get_cell_dims(img: Image, top_left: (int, int)) -> (float, float):
    """
    get_cell_dims()
    ---------------
    Prompt user for height and width in pixels of a time cell on the calendar
    based on the image provided

    :param img: the image we are considering.
    :param top_left: the user provided top left corner in (x, y) form.
    :return: a tuple of floats in the form (width, height) containing the
             dimensions of a time cell from the calendar
    """
    cropped = img.crop((top_left[0], top_left[1], img.size[0], img.size[1]))
    cropped_array = np.array(cropped)
    plt.imshow(cropped_array)
    plt.show(block=False)
    width = float(input('Please enter the width of a cell'))
    height = float(input('Please enter the height of a cell'))

    plt.close('all')
    return (width, height)


def show_cells(
    img: Image, top_left: (int, int), cell_dims: (float, float)
) -> bool:
    """
    show_cells()
    ------------
    shows the image of the calendar seperated into each time cell based on
    their provided top left crop and dimensions of a time cell.

    :param img: the image we are considering.
    :param top_left: the user provided top left conrner in (x, y) form.
    :param cell_dims: the user provided cell dimensions in (width, height) form.
    :return: boolean of if the user is happy with their provided dimensions.
    """
    img = img.crop((top_left[0], top_left[1], img.size[0], img.size[1]))
    day_time_slots = [  # yay list comprehension :)
        TimeSlot(
            top_left=Point(cell_dims[0] * i, 0),
            bottom_right=Point(cell_dims[0] * (i + 1), np.floor(cell_dims[1])),
        )
        for i in range(num_days)
    ]
    day_time_crops = []

    for day, (top, bot) in enumerate(day_time_slots):
        time_crops = []
        for time_slot in range(0, num_time_slots):
            time_crops.append(
                img.crop(
                    (
                        top.X,
                        np.floor(top.Y + time_slot * cell_dims[1]),
                        bot.X,
                        np.floor(bot.Y + time_slot * cell_dims[1]),
                    )
                )
            )
        day_time_crops.append(time_crops)

    fig, axes = plt.subplots(num_time_slots, num_days, figsize=(8, 12))
    axis_index = 0
    for i in range(num_time_slots):
        for j in range(num_days):
            axes.flat[axis_index].imshow(day_time_crops[j][i])
            axes.flat[axis_index].axis('off')
            axis_index += 1
    plt.tight_layout()
    plt.show(block=False)

    check = input(
        'Does this look like an accurate display of the cells? (y, [n]): '
    )

    return check == 'y'


def save_settings(top_left: (int, int), cell_dims: (float, float), angle: int):
    """
    save_settings()
    ---------------
    Writes the users input to the camera_constants file for use by other
    scripts in order to ensure consistency.

    :param top_left: the user provided top left corner in (x, y) form
    :param cell_dims: the user provided cell dimensions in (width, height) form
    :param angle: the user provided rotation angle of the image
    """
    with open('camera_constants.py', 'w') as file:
        file.write(f'left = {top_left[0]}\n')
        file.write(f'top = {top_left[1]}\n')
        file.write(f'time_slot_width = {cell_dims[0]}\n')
        file.write(f'time_slot_height = {cell_dims[1]}\n')
        file.write(f'rotation_angle = {angle}\n')
    print('done')


if __name__ == '__main__':
    path = sys.path[0] + '/images/calibrate.jpg'
    plt.close('all')
    cv2.destroyAllWindows()
    angle = get_rot_angle(path)
    plt.close('all')
    cv2.destroyAllWindows()
    img = Image.open(path)
    plt.close('all')
    cv2.destroyAllWindows()
    top_left = (0, 0)
    good_bounds = False
    while not good_bounds:
        plt.close('all')
        cv2.destroyAllWindows()
        top_left = get_top_left(img)
        plt.close('all')
        cv2.destroyAllWindows()
        good_bounds = show_crop(img, top_left)
        plt.close('all')
        cv2.destroyAllWindows()
    cell_dims = (
        np.floor(img.size[0] / num_days) + top_left[0],
        np.floor(img.size[1] / num_time_slots + top_left[1]),
    )
    good_bounds = False
    while not good_bounds:
        plt.close('all')
        cv2.destroyAllWindows()
        cell_dims = get_cell_dims(img, top_left)
        plt.close('all')
        cv2.destroyAllWindows()
        good_bounds = show_cells(img, top_left, cell_dims)
        plt.close('all')
        cv2.destroyAllWindows()
    save_settings(top_left, cell_dims, angle)
