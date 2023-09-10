
---
created: 2023-08-30T13:43:42
modified: 2023-09-10T11:01:29
course: General
tags: [meeting]
topics:
 - <% tp.file.cursor(2) %>
---
# General Meeting 4
- [i] course:: [[General]]
- [i] date:: 2023-08-30T13:43:42
- [i] meeting:: 4

# Agenda:
- David's showcase & Input capture milestone progress check
- Progress checks from other sub-teams

# Action Items
- [ ] Complete workplace health & safety inductions for lab @Ali
- [ ] Lock in date for workshop weekend @Dylan @Lucas
- [ ] Tape up the whiteboard @Alex @Ali
- [ ] Small individual widget designs @Maya

## David Showcase (webcam) & input capture progress check
- motion detection working (with ~1 inch sensitivity)
- once it stops detecting motion for 3seconds, it takes an image
	- can make the wait time longer
	- could we make it wait until it detects motion again? rather than every 3 seconds
- saves image as 1920x1080 pixels
- Alex just needs to make minor adjustments to the python script

- input capture on track!
- once whiteboard finalised, just need to do a bit of image normalisation
- few days behind schedule BUT the progress is a much higher standard than expected

## Dylan physical build progress check
- Workshop weekend will be needed
	- tentative dates: decide by Wednesday
- Lucas has plenty of wood offcuts
	- can buy extra plywood if needed
- can cut wood at home and do actual construction at uni
	- if timeline is tight, Lucas can construct at home (additional workshop weekend)
- not much wood working equipment at innovate
	- probably want to avoid innovate as much as possible?

## Database progress check
- currently on pause, waiting for other systems to finalise requirements

## Maya display progress check
- current design needs some more work
- LOTS of screen space, unsure how to fill completely
- security concerns -> mention in documentation and make all potential 'risky' display info optional
- gamified/'fun' widgets
	- not necessarily 'important' info but conversation starters
	- e.g. who's busiest this week
- family activity suggestions
	- gpt not free but could use meta ai - Alex happy to look into setting up if time permits
- weather app (wttr.in) outputs json, can just string splice out what we want
- slideshow picture frame widget

- have widget designs by Wednesday, can do some user feedback survey-ing around what people would choose to show

- if there is time, design and implement a nice looking config page (definitely not essential)

## UPCOMING:
### WEDNESDAY:
- lock in OHS 
- go over screen designs
- review input capture with current script
- finalise what data display team needs from DB
### NEXT SUNDAY:
- DB MVP due (revisit progress on Wednesday, can push back to following Studio if needed)
---
