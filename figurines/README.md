# Microcontroller Communications

## Windows

1. Connect the Seeduino Xiao to a serial port using provided USB-C to USB-A cable
2. Double click the [`microcontroller_communications.bat`](https://github.com/lucashicks1/lambda-deco3801/blob/main/build/figurines/microcontroller_communications.bat) file located in this directory
3. The file will download all required python libraries, so please wait for it to finish
4. The program will run on completion of installations

## Otherwise

1. Ensure you have the `lambda-env` conda environment you have from [The base readme](../README.md).
2. Otherwise, you can install the dependencies needed for this script by running the following:
```sh
pip install -r requirements.txt
```

3. Then you can start the script after connecting the Seeduino Xiao to a serial port with a
USB-C to USB-A cable. Starting the script can be done with

```sh
python microcontroller_comms.py
```
