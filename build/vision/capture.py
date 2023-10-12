import datetime
import os
import subprocess
import time

import cv2
from camera_constants import rotation_angle
from constants import python_path

# adapted from Adrian Rosebrock's tutorial on:
# https://pyimagesearch.com/2015/06/01/home-surveillance-and-motion-detection-with-the-raspberry-pi-python-and-opencv/
# Following the license found on:
# https://pyimagesearch.com/faqs/single-faq/what-is-the-code-license-associated-with-your-examples/
# A screenshot of the license is also found in assets/pyimagesearchlicense.png


cv2.destroyAllWindows()
path = './images/capture.jpg'
path = os.path.abspath(path)
cap = cv2.VideoCapture(0)
time.sleep(1.0)   # ensure webcam is opened and balanced first
noMotionTime = 0
noMotionTimeStamp = datetime.datetime.now()
avg = None
thereWasMotion = True
while True:
    truth, frame = cap.read()
    timestamp = datetime.datetime.now()
    if frame is None:
        break

    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grey = cv2.GaussianBlur(grey, (21, 21), 0)

    if avg is None:
        avg = grey.copy().astype('float')
        continue

    cv2.accumulateWeighted(grey, avg, 0.5)
    frameDelta = cv2.absdiff(grey, cv2.convertScaleAbs(avg))
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
        noMotionTimeStamp = datetime.datetime.now()
        thereWasMotion = True

    noMotionTime = timestamp - noMotionTimeStamp
    if noMotionTime > datetime.timedelta(seconds=3) and thereWasMotion is True:
        if rotation_angle == 90:
            frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
        elif rotation_angle == 180:
            frame = cv2.rotate(frame, cv2.ROTATE_180)
        elif rotation_angle == 270:
            frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
        cv2.imwrite(path, frame)
        noMotionTimeStamp = datetime.datetime.now()
        thereWasMotion = False
        vision_path = './reader.py'
        vision_path = os.path.abspath(vision_path)
        subprocess.run(f'{python_path} {vision_path} {path}', shell=True)
    # show the frame and record if the user presses a key
    cv2.imshow('Motion Detect', frame)
    key = cv2.waitKey(1) & 0xFF

    # if the `q`, or `esc` key is pressed, break from the loop
    if key == ord('q') or key == 27:
        break

# cleanup the camera and close any open windows
cap.release()
cv2.destroyAllWindows()
