# Reader Script

______________________________________________________________________

## Usage

### Setup

#### Dependencies

This program relies on the following dependencies

```
numpy
Pillow
Pytesseract
matplotlib
```

You can install these requirements and activate the environment by using the
`environment.yaml` in this directory with

```
conda env create -f environment.yaml
conda activate env
```

#### Calibration

Run the calibration script with

```
python calibrate.py
```

This will then open a matplotlib window containing a picture that you should
take manually with the camera set up in the position it will be in during program
run time.

Using this matplotlib window and image, zoom in to find the top left corner of the
calendar and record the x, y coordinate of this. Then record the height and width of
each time slot cell. Then, when prompted, enter each into the terminal after closing
the matplotlib window. Now the script should be calibrated for your current set up.

##### constants.py

Your camera may get different colour levels to mine, so if you are running into issues,
look into the `constants.py` file and change around some of the thresholds to ensure you
are not losing pixels that should be certain colours.

### Running

Run the script with

```
python reader.py local/path/to/image.jpg[png]
```

In operation, this script will is run by the motion detection program, so only needs
to be run manually in testing. This will return a .json file that will contain
every time slot that has been coloured in, with information for the day, time, colour,
and what text (if any) has been written inside the cell.
