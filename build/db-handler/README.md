# Database handler

## Overview

This database handler is a web-based RESTful API microservice which is solely responsible for all of the CRUD operations that are done on the database. As a result, all of the services that require the database will call this microservice to perform GET, POST, PATCH and DELETE operations on the database.

### Benefits

There are many benefits to a microservice approach to database interaction. They are as follows:

- **Flexibile Implementation** - As this microservice is the only service that is connected to the database, it is the only service that is required to be concerned about the implementation of the database. As a result, changes to the database structure and/or implementation only impacts one service.
- **Standardised Data** - As this is a RESTful service, this handler acts as a uniform interface of which data is accepted and sent in a standardised form. As a result, other services can expect the data to have a specified structure.
- **Load Balancing** - Easier to load balance any requests to the database, as an API gateway can be used. Although this aspect isn't hugely impactful in the project's current form, it would be invaluable if/when this project was scaled up to be used by larger audiences (eg: office spaces, etc.)
- **Managing Access** - Easier to manage specific services' access to the database. For large-scale implementations of this project, each service should only have access to resources that they require (See [PoLP](https://www.cyberark.com/what-is/least-privilege/)). For example, the service associated with controlling the movement of the figurines should only have the ability to get information from the database, and should not be able to insert data. Although this can be done on a database level, it is much easier to implement this form of access control on the database handler level.
- **Lightweight Interaction** - In order for each service to read/write information to and from the database, they will only be required to send HTTP calls when they need to, instead of establishing a connection with the database and sending requests to the database. 

### Diagram

Here is a visual representation of the interactions between the database handler and other services.

<img src="https://github.com/lucashicks1/lambda-deco3801/blob/main/assets/data-flow/Data%20Flow.png">

## Database

### Overview

For the PoC, it is intially planned for the database to be a NO-SQL document-based database to allow for greater flexibility during development. Additionally, MongoDB will be used as has great support in terms of SDKs in other languages (eg: PyMongo for python, etc.). MongoDB is not lightweight; however, this is not a major consideration as the services will be running on laptop for the PoC. For future implementations of the project that may use cloud providers (eg: AWS, Azure, GCP) a managed DB solution will be used. For example, [DocumentDB](https://aws.amazon.com/documentdb/) from AWS may be used which already has MongoDB compatability which would allow for an easier transition to cloud technology.

### Getting Started

This is eseentially how to run the mongodb server locally on your machine. This will probably be how it is done for the PoC as it is the most reliable.

#### Mac

To install MongoDB on Mac see [here](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-os-x/).

More to come here, but standard running of db should be covered in above link.

#### Windows

To install MongoDB on Windows see [here](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/)

## Microservice API

## Notes

* Have a localhost:8000/updates GET endpoint that returns either 0 or 1 to see if updates have been made

### Overview

Planning to use the FastAPI library in Python to create the web-based API. This will be running on a ASGI web server (probably Uvicorn). 

### Getting Started

#### Dependencies

Run the following to install the needed dependencies:

- `pip install fastapi`
- `pip install "uvicorn[standard]"`
- `pip install pymongo`
- `pip install pydantic`


#### Running the server

To run the server that is serving the API, run the following: 

`uvicorn app.main:app --reload`

*Note: If you have issues where uvicorn can't be found, run* `python -m uvicorn app.main:app --reload`


- *{main}* - name of the python file that has the FastAPI app instance
- *{app}* - name of the FastAPI instance
- *--reload* - flag to force the server to reload everytime changes are made - helpful during dev

### Interaction

To interact with this server, you need to make HTTP calls to it.

The following code is an example of how to do a post HTTP call in python (you may need to install the `requests` library as it is not standard). For more info see [here](https://requests.readthedocs.io/en/latest/)

```Python
import requests

# Data in a normal python dictionary
data = {"key1": 1, "key2": 2}

# Send data as request body through json parameter
response = requests.post("localhost:8000/testEndpoint", json=data)
```

# Overview on db structure

## Events

Both individual events and family events will be stored in the database in the same collection.

```JSON
{
    "day": "monday",
    "time_slot": "09:45",
    "booked_users": ["user_1", "user_3"]
}
```

For family events, the `"family"` string will be stored in array stored under the `booked_users` key. Additionally, for family events with a description, a `"description"` key-value pair will be added to the timeslot document.
```JSON
{
    "day": "monday",
    "time_slot": "09:45",
    "booked_users": ["user_1", "user_3", "family"],
    "description": "Timmy's birthday"
}
```

## Data use-cases

### Figures

* GET endpoint to check if any updates were made -> if so figure display
* Get all booked users for a specific timeslot

### Clock Face Display Screen


### Family lambda-board

* GET aggregated calendar info -> could transform data into time chunks (eg: 1 document per 15 minute block)
* POST timeslots to block out everyones availability

### Individual lambda-board

* GET an individuals timeslots (eg: find timeslots were a user is busy/booked)
* POST a timeslot for a specific user