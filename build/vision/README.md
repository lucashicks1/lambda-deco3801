
For explanation of how the defisheye code works see the original [repo](https://github.com/NSEvent/defisheye)

Install required python packages with 
```
conda install -f environment.yaml
```


Then simply run 
```
python reader.py
```
This will look for the most recent image that has been added to the images directory. Then apply
the defisheye effect to straighten up the image, and then extract the information from the calendar
and return a json formatted information for coloured trime slots for use with the database.
