# import the necessary packages
import imutils
import datetime
import json
import time
import cv2

# adapted from Adrian Rosebrock's tutorial on:
# https://pyimagesearch.com/2015/06/01/home-surveillance-and-motion-detection-with-the-raspberry-pi-python-and-opencv/

vs = cv2.VideoCapture(1, cv2.CAP_DSHOW)
vs.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
vs.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
time.sleep(1.0)
noMotionTime = 0
noMotionTimeStamp = datetime.datetime.now()
avg = None
thereWasMotion = True
while True:
    _, frame = vs.read()
    timestamp = datetime.datetime.now()
    if frame is None:
        break

    frame = imutils.resize(frame, width=1920, height=1080)
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grey = cv2.GaussianBlur(grey, (21, 21), 0)

    if avg is None:
        avg = grey.copy().astype("float")
        continue

    cv2.accumulateWeighted(grey, avg, 0.5)
    frameDelta = cv2.absdiff(grey, cv2.convertScaleAbs(avg))
    thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)

    contours = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)

    for c in contours:
        if cv2.contourArea(c) < 500:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        noMotionTimeStamp = datetime.datetime.now()
        thereWasMotion = True

    noMotionTime = timestamp - noMotionTimeStamp
    if noMotionTime > datetime.timedelta(seconds=3) and thereWasMotion is True:
        text = timestamp.strftime("%A %d %B %Y %I:%M:%S%p")
        cv2.putText(frame, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.imwrite("test.png", frame)
        noMotionTimeStamp = datetime.datetime.now()
        thereWasMotion = False
    # show the frame and record if the user presses a key
    cv2.imshow("Epic Motion Epicness Detection Camera", frame)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key is pressed, break from the loop
    if key == ord("q"):
        break

# cleanup the camera and close any open windows
vs.release()
print("gonna end")
cv2.destroyAllWindows()
print("ended")
