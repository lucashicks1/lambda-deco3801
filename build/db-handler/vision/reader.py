from PIL import Image
import json
import matplotlib.pyplot as plt
import numpy as np
import pytesseract

days_of_the_week = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}


def main(image: Image):
    threshold = 100  # TODO This is summed RGB values. Think of intensity
    rgb_image = image.convert("RGB")
    # TODO Once opened, or maybe after closed. We should move image out of this
    # folder

    """
    This will contain real tuples of start x, y and end x, y defining top
    left and bottom right corners of pixel locations for each time slot.
    TODO: Consider a way to automate this? Maybe using a class approach?
    """
    day_time_slots = [
        ((420 * 0, 0), (420 * 1, 480)),
        ((420 * 1, 0), (420 * 2, 480)),
        ((420 * 2, 0), (420 * 3, 480)),
        ((420 * 3, 0), (420 * 4, 480)),
        ((420 * 4, 0), (420 * 5, 480)),
        ((420 * 5, 0), (420 * 6, 480)),
        ((420 * 6, 0), (420 * 7, 480)),
    ]
    day_time_crops = []
    coloured_time_slots = []
    time_slot_height = 480

    for day, (top_left, bottom_right) in enumerate(day_time_slots):
        time_crops = []
        for time_slot in range(0, 5):
            time_slot_crop = image.crop(
                (
                    top_left[0],
                    top_left[1] + time_slot * time_slot_height,
                    bottom_right[0],
                    bottom_right[1] + time_slot * time_slot_height,
                )
            )
            time_slot_array = np.array(time_slot_crop)
            time_slot_size = time_slot_array.shape[0] * time_slot_array.shape[1]
            threshold_mask = (time_slot_array <= threshold).all(axis=-1)
            num_coloured = np.sum(threshold_mask)
            is_coloured = (num_coloured / time_slot_size) * 100 >= 3
            time_crops.append((time_slot_crop, is_coloured))
            if is_coloured:
                ocr_result = pytesseract.image_to_string(time_slot_crop)
                coloured_time_slots.append(
                    {
                        "day": days_of_the_week.get(day),
                        "time_slot": time_slot,
                        "data": ocr_result,
                    }
                )
        day_time_crops.append(time_crops)
    fig, axes = plt.subplots(5, 7, figsize=(8, 12))
    axis_index = 0
    print("Mon\tTue\tWed\tThu\tFri\tSat\tSun")
    for time in range(5):
        print(
            f"{day_time_crops[0][time][1]}\t{day_time_crops[1][time][1]}\t{day_time_crops[2][time][1]}\t{day_time_crops[3][time][1]}\t{day_time_crops[4][time][1]}\t{day_time_crops[5][time][1]}\t{day_time_crops[6][time][1]}"
        )
    for i in range(5):
        for j in range(7):
            axes.flat[axis_index].imshow(day_time_crops[j][i][0])
            axes.flat[axis_index].axis("off")
            axis_index += 1
    plt.tight_layout()
    plt.show()
    with open("coloured_time_slots.json", "w") as json_file:
        json.dump(coloured_time_slots, json_file, indent=4)


def normalise_image() -> Image:
    img_path = "./PXL_20230905_085907760.MP.jpg"
    img = Image.open(img_path)

    left = 73
    top = 809
    bottom = 3258
    right = 3010

    img = img.crop((left, top, right, bottom))
    img_array = np.array(img)
    threshold = 150

    white_mask = (img_array >= threshold).all(axis=-1)
    img_array[white_mask] = [255, 255, 255]
    img_array[~white_mask] = [0, 0, 0]
    new_img = Image.fromarray(img_array)

    return new_img


if __name__ == "__main__":
    image = normalise_image()
    # plt.imshow(image)
    # plt.grid("on")
    # plt.show()
    main(image)
