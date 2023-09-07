import cv2 as cv

cam_port = 1
cam = cv.VideoCapture(cam_port)

result, image = cam.read()

if result:
  
    # showing result, it take frame name and image 
    # output
    cv.imshow("GeeksForGeeks", image)
  
    # saving image in local storage
    cv.imwrite("GeeksForGeeks.png", image)
  
    # If keyboard interrupt occurs, destroy image 
    # window
    cv.waitKey(0)
    cv.destroyWindow("GeeksForGeeks")
  
# If captured image is corrupted, moving to else part
else:
    print("No image detected. Please! try again")
