import cv2
import numpy as np

# import math
# import pytesseract
# import json


def find_contours(path: str):
    image = cv2.imread(path)
    grey_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(grey_scale, 50, 325, None, 3)
    contours, _ = cv2.findContours(
        edges,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE,
    )
    result = image.copy()
    min_contour_area = 500
    contours = [
        contour
        for contour in contours
        if cv2.contourArea(contour) > min_contour_area
    ]
    time_slot_array = []
    cv2.drawContours(result, contours, -1, (0, 255, 255), 5)
    cv2.imshow("contours", result)
    cv2.waitKey()
    cv2.destroyAllWindows()
    for i, contour in enumerate(contours):
        rot_rect = cv2.minAreaRect(contour)
        box = cv2.boxPoints(rot_rect)
        box = np.intp(box)
        time_slot_array.append(
            image[box[0][0] : box[2][0], box[1][1] : box[3][1], :],
        )
        # cv2.imshow("image", image[box[0][0] : box[2][0], box[1][1] : box[3][1], :])
        # cv2.waitKey()
        # cv2.destroyAllWindows()
    return time_slot_array


def display_images(images):
    print(len(images))
    # while True:
    #     cv2.imshow(f'image {i}', image)
    #     k = cv2.waitKey(33)
    #     if k == 27:  # Need to press escape to stop
    #         cv2.destroyAllWindows()
    #         break
    #     else:
    #         continue


if __name__ == '__main__':
    time_slot_array = find_contours('./images/test1.jpg')
    display_images(time_slot_array)
