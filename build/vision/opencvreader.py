import cv2
import matplotlib.pyplot as plt
from tqdm import tqdm
import math
import pytesseract
import json
import numpy as np


def find_contours(path: str):
    image = cv2.imread(path)
    grey_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(grey_scale, 150, 625, None, 3)
    contours, _ = cv2.findContours(
        edges,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE,
    )
    result = image.copy()
    min_contour_area = 500
    contours = [
        contour for contour in contours if cv2.contourArea(contour) > min_contour_area
    ]
    time_slot_array = []

    for i, contour in enumerate(contours):
        rot_rect = cv2.minAreaRect(contour)
        box = cv2.boxPoints(rot_rect)
        box = np.intp(box)
        time_slot_array.append(
            image[box[0][0] : box[3][0], box[0][1] : box[3][1], :],
        )
    return time_slot_array


def display_images(images):
    montage_height = 0
    montage_width = 0
    print(len(images))
    for image in images:
        montage_height = max(image.shape[0], montage_height)
        montage_width = max(image.shape[1], montage_width)

    montage = np.zeros((montage_height, montage_width, 3), dtype=np.uint8)

    height_so_far = 0
    width_so_far = 0
    for i, image in enumerate(images):
        montage[
            height_so_far : height_so_far + image.shape[0],
            width_so_far : width_so_far + image.shape[1],
            :,
        ] = image
        height_so_far += image.shape[0]
        width_so_far += image.shape[1]

    cv2.imshow("montage", montage)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    time_slot_array = find_contours("./images/test3.jpg")
    display_images(time_slot_array)
