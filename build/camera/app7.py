# import the necessary packages
import imutils
import argparse
import datetime
import json
import time
import cv2


vs = cv2.VideoCapture(1, cv2.CAP_DSHOW)
time.sleep(1.0)
noMotionTime = 0
noMotionTimeStamp = datetime.datetime.now()
avg = None
while True:
    _, frame = vs.read()
    timestamp = datetime.datetime.now()
    if frame is None:
        break

    frame = imutils.resize(frame, width=500)
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grey = cv2.GaussianBlur(grey, (21, 21), 0)

    if avg is None:
        avg = grey.copy().astype("float")
        continue

    cv2.accumulateWeighted(grey, avg, 0.5)
    frameDelta = cv2.absdiff(grey, cv2.convertScaleAbs(avg))
    thresh = cv2.threshold(frameDelta, 15, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)

    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        if cv2.contourArea(c) < 500:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        noMotionTimeStamp = datetime.datetime.now()

    noMotionTime = timestamp - noMotionTimeStamp
    if noMotionTime > datetime.timedelta(seconds=10):
        cv2.imwrite("test.png", frame)
        noMotionTimeStamp = datetime.datetime.now()
    # show the frame and record if the user presses a key
    cv2.imshow("Security Feed", frame)
    #cv2.imshow("Thresh", thresh)
    #cv2.imshow("Frame Delta", frameDelta)
    key = cv2.waitKey(1) & 0xFF

    # if the `q` key is pressed, break from the loop
    if key == ord("q"):
        break

# cleanup the camera and close any open windows
vs.release()
print("gonna end")
cv2.destroyAllWindows()
print("ended")