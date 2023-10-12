import datetime
import os
import subprocess
import time
from argparse import ArgumentParser
from dataclasses import dataclass
from typing import Union

import cv2
import numpy as np
from camera_constants import rotation_angle
from constants import python_path

# adapted from Adrian Rosebrock's tutorial on:
# https://pyimagesearch.com/2015/06/01/home-surveillance-and-motion-detection-with-the-raspberry-pi-python-and-opencv/
# Following the license found on:
# https://pyimagesearch.com/faqs/single-faq/what-is-the-code-license-associated-with-your-examples/
# A screenshot of the license is also found in assets/pyimagesearchlicense.png


@dataclass
class MotionInfo:
    """
    This class is used for containing the information about when motion has
    happened etc. Mostly used as a concise way of passing information around
    """
    noMotionTime: datetime.timedelta
    noMotionTimeStamp: datetime.datetime
    avg: np.ndarray
    thereWasMotion: bool
    v: bool
    t: bool


parser = ArgumentParser(description='Capture data, with optional flags')
parser.add_argument(
    '-v', '--visualise', action='store_true', help='Enable visualiser mode'
)
parser.add_argument(
    '-t', '--time', action='store_true', help='Enable timer for reader.py'
)
args = parser.parse_args()


def do_cap(v: bool, t: bool):
    """
    do_cap()
    --------
    Performs the capture operations and contains the main loop

    :param v: the visualise flag
    :param t: the time flag
    """
    cap = cv2.VideoCapture(0)
    time.sleep(1.0)   # ensure webcam is opened and balanced first
    motion = MotionInfo(0, datetime.datetime.now(), None, True, v, t)
    while not isinstance(motion, bool):
        motion = detect_motion(cap, motion)

    # cleanup the camera and close any open windows
    cap.release()
    cv2.destroyAllWindows()


def detect_motion(
    cap: cv2.VideoCapture, motion: MotionInfo
) -> Union[bool, MotionInfo]:
    """
    detect_motion()
    ---------------
    This method handles the logic for detecting motion and when to prompt to take
    an image and process the information.

    :param cap: the cv2.VideoCapture object that is the cameras current output
    :param motion: a MotionInfo object containing all important info about the current
                  running
    :return: the MotionInfo object with updated values.
    """
    _, frame = cap.read()
    timestamp = datetime.datetime.now()
    if frame is None:
        # implies frame get error. Need to break out of program
        return False

    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grey = cv2.GaussianBlur(grey, (21, 21), 0)

    if motion.avg is None:
        motion.avg = grey.copy().astype('float')
        return motion

    cv2.accumulateWeighted(grey, motion.avg, 0.5)
    frameDelta = cv2.absdiff(grey, cv2.convertScaleAbs(motion.avg))
    thresh = cv2.threshold(frameDelta, 15, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)

    (contours, *_) = cv2.findContours(
        thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    for c in contours:
        if cv2.contourArea(c) < 500:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        motion.noMotionTimeStamp = datetime.datetime.now()
        motion.thereWasMotion = True

    motion.noMotionTime = timestamp - motion.noMotionTimeStamp
    if (
        motion.noMotionTime > datetime.timedelta(seconds=3)
        and motion.thereWasMotion is True
    ):
        take_image(frame, motion)

    # if visualise option: show the frame and record if the user presses a key
    if motion.v:
        cv2.imshow('Motion Detect', frame)
        key = cv2.waitKey(1) & 0xFF

        # if the `q`, or `esc` key is pressed, break from the loop
        if key == ord('q') or key == 27:
            return False

    return motion


def take_image(frame: np.ndarray, motion: MotionInfo):
    """
    take_image()
    ------------
    Takes the image, rotates it appropriately, then saves it to the path directory

    :param frame: the ndarray created by reading the current frame of the camera
    :param motion: the MotionInfo object with important information
    """
    if rotation_angle == 90:
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    elif rotation_angle == 180:
        frame = cv2.rotate(frame, cv2.ROTATE_180)
    elif rotation_angle == 270:
        frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    cv2.imwrite(path, frame)
    motion.thereWasMotion = False
    motion.noMotionTimeStamp = datetime.datetime.now()
    subprocess.run(f'{python_path} {vision_path} {path}', shell=True)
    # if time option: print time it takes to run reader script
    if motion.t:
        print(datetime.datetime.now() - motion.noMotionTimeStamp)


if __name__ == '__main__':
    cv2.destroyAllWindows()
    path = './images/capture.jpg'
    path = os.path.abspath(path)
    vision_path = './reader.py'
    vision_path = os.path.abspath(vision_path)

    do_cap(args.visualise, args.time)
