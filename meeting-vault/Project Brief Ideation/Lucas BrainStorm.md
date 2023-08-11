# Project Overview
## 1. Calendar Data Store
### 1.1 Structure
- Either use NoSQL or SQL database - if NoSQl probs document-based
- NoSQL database will most likely be nicer to work with and allow for much more flexibility - in case data changes or extra fields need to be added
- Couple of options for DBs
	- Host our own mongo flavour - could be payload as not managed
	- Go for a managed instance in the cloud - Firestore in GCP, DocumentDB in AWS, Cosmo in Azure
	- Could use Azure's free student plan thing - I've got $150 USD to credit
	- If using GCP, could bundle cloud resource in Google Project created for getting API access - but GCP sucks
- Need to figure out how to connect microcontroller to db
	- Whether it can get a connection directly to db
	- or have the data grabbed from another bit of hardware and just pass the data in easily

### 1.2 Example Payload from gCal - could use as reference
```
{
    'summary': 'Event summary',
    'location': 'test location',
    'description': 'test Description',
    'start': {
        'dateTime': '2015-05-28T09: 00: 00-07: 00',
        'timeZone': 'America/Los_Angeles',
    },
    'end': {
        'dateTime': '2015-05-28T17: 00: 00-07: 00',
        'timeZone': 'America/Los_Angeles',
    },
    'attendees': [
        {
            'email': 'attendee1@example.com'
        },
        {
            'email': 'attendee2@example.com'
        },
    ]
}
```

## 2. Figurine Display
### 2.1 Date Slider
### 2.2 Calendar Data Poller
- Slightly mentioned at the bottom of 1.1 - will need to draw diagram for this
### 2.3 Figure Elevator
### 2.4 Figurines

## 3. gCal Scraper
### 3.1 API overview
- Will be using Google Calendar API - [View here](https://developers.google.com/calendar/api/guides/overview)
- I have already setup google project and added API
- Have done basic OAuth page
- Will need to figure out how to individually gain auth for users
	- do it manually
	- create some basic as web app allow registration to scraper and give it access
- 

### 3.2 Scraper Overview
- Could write in a couple of different languages
	- Python would be the simplest
	- Go would be nice as thats what cool people write stuff in
	- Java - but why????
	- JS - but also why????
- Need to run on some sort of schedule
- Ideally if we are already running cloud 

### 3.3 Scraper Process

### 3.4 Scraper Infra + Implementation

## 4. Interactive calendar input (whiteboard)
