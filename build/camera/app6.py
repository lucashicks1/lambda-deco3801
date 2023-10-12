import time

import cv2 as cv

cam_port = 1
cam = cv.VideoCapture(cam_port, cv.CAP_DSHOW)
cam.set(cv.CAP_PROP_FRAME_WIDTH, 352)
cam.set(cv.CAP_PROP_FRAME_HEIGHT, 288)

result, image = cam.read()
result2 = cam.isOpened()
print(result, result2)
time.sleep(2.0)
if result:
    print('cam read')
    # showing result, it take frame name and image
    # output
    cv.imshow('test', image)

    # saving image in local storage
    # cv.imwrite("test.png", image)

    # If keyboard interrupt occurs, destroy image
    # window
    cv.waitKey(0)
    cv.destroyWindow('test')

# If captured image is corrupted, moving to else part
else:
    print('No image detected. Please! try again')
