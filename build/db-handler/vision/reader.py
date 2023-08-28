from PIL import image
import json
import numpy as np

days_of_the_week = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}


def is_coloured(pixel: (float,), threshold: float) -> bool:
    """
    is_coloured()
    -------------
    A function to determine if our time block has been coloured in to be
    marked as busy or not.
    """
    return sum(pixel) > threshold


def main():
    threshold = 100  # TODO This is summed RGB values. Think of intensity
    image_path = "./current/current.png"  # TODO set an actual file name
    image = Image.open(image_path)
    rgb_image = image.convert("RGB")
    # TODO Once opened, or maybe after closed. We should move image out of this
    # folder

    day_time_slots = [
        """
        This will contain real tuples of start x, y and end x, y defining top
        left and bottom right corners of pixel locations for each time slot.
        TODO: Consider a way to automate this? Maybe using a class approach?
        """(
            (0, 0), (140, 30)
        ),
    ]
    coloured_time_slots = []
    time_slot_width = 140  # TODO Can also maybe be automated?

    for day, (top_left, bottom_right) in enumerate(day_time_slots):
        for time_slot in range(0, 23):  # 24 hour times
            x = top_left[0] + time_slot * time_slot_width
            y = top_left[1]

            pixel_colour = rgb_image.getpixel(x, y)
            if is_coloured(pixel_colour, threshold):
                coloured_time_slots.append({
                    'day': days_of_the_week.get(day),
                    'time_slot': time_slot,
                    'colour': pixel_colour
                    })
    with open('coloured_time_slots.json', 'w') as json_file:
        json.dump(coloured_time_slots, json_file, indent=4)


if __name__ == "__main__":
    main()
