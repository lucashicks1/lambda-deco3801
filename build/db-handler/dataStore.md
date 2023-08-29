# Overview on db structure

## Family events

* Torn on how to display time, mongo has DateTime but date is ugly

{
    "day": "monday",
    "start_time": "09:15",
    "end_time": "09:45",
    "description:
}


## Individual events

* Assume that for the individual events, blocks are always 15 minutes long (eg: start at 9:15, go till 9:30)

{
    "day": "monday",
    "time": "09:15",
    "booked_users": ["user_1", "user_3"]
}

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