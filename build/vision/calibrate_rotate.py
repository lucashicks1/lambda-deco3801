import sys

import cv2


def get_rot_angle(path: str) -> int:
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
    return angle


def save_settings(angle: int):
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
        file.write(f'rotation_angle = {angle}\n')
    print('done')


if __name__ == '__main__':
    path = sys.path[0] + '/images/calibrate.jpg'
    angle = get_rot_angle(path)
    save_settings(angle)
