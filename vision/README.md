# Dependencies

These programs rely on the following libraries

```
numpy
Pillow
Pytesseract
opencv-python-headless
```

The calibration script relies on the above, as well as

```
matplotlib
```

For your convenience, there is an `environment.yaml` for you to create a conda
virtual environment with our libraries installed already for this section.
You can create and activate this environment with the following.

```
conda env create -f environment.yaml
conda activate lambda-vision
```

Or you can create your own environment and install the packages with

```conda create -n your_env_name
conda activate your_env_name
conda install numpy pillow pytesseract matplotlib
pip install opencv-python-headless
```

When installation of dependencies is complete, from the environment you are using
run

```
which python
```

and put the result of that into constants.py in place of python_path

# Reader Script

This script uses an image of the calendar and given some presets created by a
calibration script will go through the image and look at each time slot in the
calendar and determine if there is anything written in each cell. If something
is, then it will record what colour (red, blue, or black) and if applicable, will
use Pytesseract for OCR and save the text written in the cell.

This information is then saved in json format and sent as a request to the database

## Usage

### Setup and calibration

First run the `calibrate_rotate.py` script to get a rotation angle. Then run the `calibrate.py`
script to set the top-left corner and the cell height and width. Run these scripts with

```
python calibrate_rotate.py
python calibrate.py
```

This will then open a open cv window containing a picture that you should
take manually with the camera set up in the position it will be in during program
run time. Using this you can decide on a rotation angle for the image (must be one
of 0, 90, 180, or 270) in degrees for a clockwise rotation.

Then the program will open a matplotlib window with an image taken at this rotation
angle

Using this matplotlib window and image, zoom in to find the top left corner of the
calendar (as in the top left corner of the top left most time slot, not in the column
or row names) and record the x, y coordinate of this. Then record the height and width of
each time slot cell. Then, when prompted, enter each into the terminal after closing
the matplotlib window. Now the we have the calibration for your set up.

##### [constants.py](./constants.py)

Your camera may get different colour levels to mine, so if you are running into issues,
look into the `constants.py` file and change around some of the thresholds to ensure you
are not losing pixels that should be certain colours.

### Running capture

This script is typically run by `capture.py` but if you want to manually check if the
program works in debugging, you can do this with:

```
python reader.py local/path/to/image.jpg
```

# Capture Script

This is the main script that handles opening the webcam, detecting movement. Then
taking an image when there is no movement detected for 1 second (after movement).
This prevents having to process images when nothing has changed, and also ensures
we wait until after the user has finished with the whiteboard before processing
an image.

## Usage

As this script calls [reader.py](#reader-script), we need to ensure we have first done the usage
instruction in its [section](#setup-and-calibration)

### Running

We can then run the script with

```
python capture.py [-v] [-t]
```

The optional arguments give power over the following

- \[-v\] - visualiser. This will open a cv2 window to see what the camera
  is seeing as well as where the motion detected contours are. For use in troubleshooting.
- \[-t\] - timer. This will control printing to stdout how long it takes for the
  reader script to process an image. For use in trouble shooting and optimisation tests.
