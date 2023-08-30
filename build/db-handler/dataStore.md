# Overview on db structure

## Events

Both individual events and family events will be stored in the database in the same collection.

```JSON
{
    "day": "monday",
    "start_time": "09:45",
    "booked_users": ["user_1", "user_3"]
}
```

For family events, the `"family"` string will be stored in array stored under the `booked_users` key. Additionally, for family events with a description, a `"description"` key-value pair will be added to the timeslot document.
```JSON
{
    "day": "monday",
    "start_time": "09:45",
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
