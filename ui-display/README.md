# UI Display

## Frontend App

This is the display that goes inside of the clock as our output node.
Keep in mind this was designed for a 1920x1080 screen that has been rotated to be portrait — this is possible in almost all recent versions of popular web browsers (for reference, we used Google Chrome), so feel free to look up your preferred browser in order to find instructions for doing so, but also note that you can achieve nearly the same effect by resizing the screen.

Also, please be aware that because of the limited use case in which our screen is to be deployed (i.e. in a fixed size wooden housing with no intentional provisions for system users to directly control or resize the screen themselves), the prototype version of the app is not consistently responsive, and in some cases uses fixed dimensions to set styles. This was a design decision made by the front-end development team due to the project scope; we felt given the very specific constraints our system places on display interactions, features intended for 'normal' web app interactivity such as responsiveness were not a priority. However, a production version of the product would take a more generalisable approach that would be compatible with multiple different module resolutions. 

### Running the app 

First you will need to follow the [Node setup instructions](../README.md#node-requirements). Then you can either run the app via the development server (which enables hot reloading if you intend to make code changes, and retains the original source code) by entering the following:

```sh
cd frontend-app
npm start
``` 
Or, you can generate a minified distributable bundle of the web app, refered to as the "build" version, via the following commands:

```sh
cd frontend-app
npm run build
serve -s build
```

Both of these will start the web app on `localhost:3000`, which should be printed to you when you first
serve the build. As mentioned in the top-level repository readme, you should also make sure to run the database server first, as the majority of the screen widgets will print an error or loading message rather than rendering any components if the database cannot be reached. 

## Distribution Test 

This app is a minified build version of the screen prototype, now deprecated by a few versions but appropriate for some trivial testing. 
