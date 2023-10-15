# BUILD
Build code goes here when project underway

## Initial Environment Setup
Our project relies on several different libraries in order for it to function. As most of our project is written in Python, there is an [`environment.yaml`](https://github.com/lucashicks1/lambda-deco3801/blob/main/environment.yaml) file that has been created, allowing you to create your own conda virtual environment. You can create and activate this environment with the following:

```
conda env create -f environment.yaml
conda activate lambda-env
```
Or you can create your own environment and install the packages with

```
conda create -n your_env_name
conda activate your_env_name
conda install numpy pillow pytesseract matplotlib pymongo requests
conda install -c conda-forge fastapi pydantic uvicorn-standard
pip install opencv-python-headless
```

Once this environment is setup, all the needed dependencies for our python components should be installed.

## Build Instructions for each project component
1. [Database](../build/db-handler/README.md)
2. [Camera](../build/vision/README.md)
3. [Display](../build/ui-display/frontend-app/README.md)
4. [Microcontroller](../build/microcontroller/README.md)
5. [Microcontroller Communication](../build/figurines/README.md)

### If any further details are required, please contact a member of Team \Lambda
