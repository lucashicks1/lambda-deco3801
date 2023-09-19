import cv2

image = cv2.imread('./images/test1.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blurred = cv2.GaussianBlur(gray, (5, 5), 0)

edges = cv2.Canny(blurred, 50, 150)

contours, _ = cv2.findContours(
    edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
)

filled_cells = []
empty_cells = []

for contour in contours:
    area = cv2.contourArea(contour)

    if area > 500:
        filled_cells.append(contour)
    else:
        empty_cells.append(contour)


for contour in filled_cells:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)

for contour in empty_cells:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 3)

cv2.imwrite('./outputs/test.jpg', image)
