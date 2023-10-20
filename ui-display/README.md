# UI Display

## Frontend App

This is the display that goes inside of the clock as our output node.
Keep in mind this was designed for a 1920x1080 screen that has been rotated to be portrait.

### Run

First you will need to follow the [Node setup instructions](../README.md#node-requirements), then you can enter the following:

```sh
cd frontend-app
npm run build
serve -s build
```

This will start the web app on `localhost:3000` which should be printed to you when you first
serve the build.

## Distribution Test

This app is mostly just for testing. Not used in the main running of our program
