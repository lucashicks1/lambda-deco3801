# Database handler

## Overview

This database handler is a web-based RESTful API microservice which is solely responsible for all of the CRUD operations that are done on the database. As a result, all of the services that require the database will call this microservice to perform GET, POST, PATCH and DELETE operations on the database.

## Getting Started

### Installation

You need a couple of dependencies if you want to run the uvicorn server locally to serve the API. Run these options:

1. Install using conda environment

For convinience, a conda environment has been created so that all project dependencies can be installed using as few commands as possible. See more on this option [here](https://github.com/lucashicks1/lambda-deco3801/blob/main/build/vision/README.md#dependencies)

2. Install with `requirements.txt`:

`pip install -r requirements.txt`

3. Install all dependencies individually:

`pip install fastapi pymongo pydantic "uvicorn[standard]"`

*Note: A python environment with every project dependency is available for use, so this step could be skipped if the other environment is set up.*

### Database Setup
This API microservice uses either a local monogbd database or a remote database hosted in the cloud. If the microservice is unable to connect to the remote instance running in the cloud, it will connect to the local database as a backup.

#### Cloud instance
To enable the app to connect to the remote database, your application must be authenticated with the database. In order to not store database secrets in the code repository, these secrets (username, password) are loaded in from your environment. Therefore you must set both the `DB_USER` and `DB_PASS` environment variables to the correct values.

**\<USERNAME\> and \<PASSWORD\> are both placeholders. To obtain the actual values, please contact team Lambda.**

On a mac/linux machine to set a temporary environment variable run the following in your shell:

```
export DB_USER=<USERNAME>
export DB_PASS=<PASSWORD>
```

#### Remote instance

##### Installation
If you want to connect to a local database instance, you must first install mongodb on your system and then must run it.

To install mongodb on your computer, follow the appropriate guide for your system:
- [Mac](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/#install-mongodb-community-edition)
- [Windows](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/#install-mongodb-community-edition)
- [Linux](https://www.mongodb.com/docs/manual/administration/install-on-linux/)

*Note: If you are installing this on a linux machine, take careful note of your distribution as different distributions require different installation procedures.*

##### Run

Once installed, run mongodb using the following guides:
- [Mac](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/#run-mongodb-community-edition)
- [Windows](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/#run-mongodb-community-edition-as-a-windows-service)

*Note: for linux distributions follow the installation guide you used to run the database.*

## Running the API

To run the API, ensure that you are in the [`db-handler`](https://github.com/lucashicks1/lambda-deco3801/tree/main/build/db-handler) directory. Once you are in this directory, run the following command:

`uvicorn app.main:app`

*Note: If you have issues with you python installation and uvicorn can't be found, run `python -m uvicorn app.main:app`.

- `{app.main}` - location of the python file that contains the FastAPI app
- `{app}` - name of the FastAPI app instance in the file
- `--reload` - optional flag that can be used when running the uvicorn server, so that it reloads after any changes are made to the directory 
- `--port XXXX` - optional flag to specify what port the server will run on - port 8000 by default


## Database

### Overview

MongoDB database running locally.

* Database name: *mydb*
* Collection name(s): *users*, *calendar*

### DB Structure

Both individual events and family events will be stored in the database in the same collection.

```JSON
{
    "day": "monday",
    "time_slot": "07:00",
    "slot_num": 27,
    "booked_users": ["user_1", "user_3"]
}
```

For family events, the `"family"` string will be stored in array stored under the `booked_users` key. Additionally, for family events with a description, a `"description"` key-value pair will be added to the timeslot document.
```JSON
{
    "day": "monday",
    "time_slot": "07:00",
    "slot_num": 27,
    "booked_users": ["user_1", "user_3", "family"],
    "description": "Timmy's birthday"
}
```

## Microservice

### Overview

Planning to use the FastAPI library in Python to create the web-based API. This will be running on a ASGI web server (probably Uvicorn). 

### Example Interaction with Microservice

To interact with this server, you need to make HTTP calls to it.

The following code is an example of how to do a post HTTP call in python (you may need to install the `requests` library as it is not standard). For more info see [here](https://requests.readthedocs.io/en/latest/)

```Python
import requests

# Data in a normal python dictionary
data = {"key1": 1, "key2": 2}

# Send data as request body through json parameter
response = requests.post("localhost:8000/testEndpoint", json=data)
```

### Benefits

There are many benefits to a microservice approach to database interaction. They are as follows:

- **Flexibile Implementation** - As this microservice is the only service that is connected to the database, it is the only service that is required to be concerned about the implementation of the database. As a result, changes to the database structure and/or implementation only impacts one service.
- **Standardised Data** - As this is a RESTful service, this handler acts as a uniform interface of which data is accepted and sent in a standardised form. As a result, other services can expect the data to have a specified structure.
- **Load Balancing** - Easier to load balance any requests to the database, as an API gateway can be used. Although this aspect isn't hugely impactful in the project's current form, it would be invaluable if/when this project was scaled up to be used by larger audiences (eg: office spaces, etc.)
- **Managing Access** - Easier to manage specific services' access to the database. For large-scale implementations of this project, each service should only have access to resources that they require (See [PoLP](https://www.cyberark.com/what-is/least-privilege/)). For example, the service associated with controlling the movement of the figurines should only have the ability to get information from the database, and should not be able to insert data. Although this can be done on a database level, it is much easier to implement this form of access control on the database handler level.
- **Lightweight Interaction** - In order for each service to read/write information to and from the database, they will only be required to send HTTP calls when they need to, instead of establishing a connection with the database and sending requests to the database. 

### Process Diagram

Here is a visual representation of the interactions between the database handler and other services.

<img src="https://github.com/lucashicks1/lambda-deco3801/blob/main/assets/data-flow/Data%20Flow.png">


### Data use-cases

#### Figures

* GET endpoint to check if any updates were made -> if so figure display
* Get all booked users for a specific timeslot

#### Clock Face Display Screen


#### Family lambda-board

* GET aggregated calendar info -> could transform data into time chunks (eg: 1 document per 15 minute block)
* POST timeslots to block out everyones availability

#### Individual lambda-board

* GET an individuals timeslots (eg: find timeslots were a user is busy/booked)
* POST a timeslot for a specific user