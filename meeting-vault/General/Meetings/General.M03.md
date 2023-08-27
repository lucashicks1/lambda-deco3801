
---
created: 2023-08-27T11:04:15
modified: 2023-08-27T11:04:15
course: General
tags: [meeting]
topics:
 - <% tp.file.cursor(2) %>
---
# General Meeting 3
- [i] course:: [[General]]
- [i] date:: 2023-08-27T11:04:15
- [i] meeting:: 3

# Agenda:
- Whiteboard discussion
- Presentation
- Database schema progress
- Next technical steps
- Display discussion
# Action Items
- [x] join figma team @Maya
- [ ] send Alex json format for input data @Lucas
- [ ] begin Computer Vision investigation/implementation @Alex
- [ ] have some sketches prepped to discuss at Wednesday  meeting @Maya
- [ ] begin database creation to discuss at Wednesday meeting @Lucas @David
- [ ] begin design/build @Dylan
- [ ] finalise presentation @Ali @Alex
- [ ] begin user research write up @Ali
- [ ] Review git hub roadmap @ALL
# Questions for Rosti
- Should we demo an individual calendar or focus on the collaboration/family calendar?
	- our solution does have the individual calendars, but the family one is the only one we would demo
- List of equipment to rent (see Teams chat)
## Whiteboard discussion
- purchased blank whiteboard this morning
- will sketch in grid and secure in with thin electrical tape
- 15 min time slots are too small -> use 30 min or 1 hr intervals
- lose 5x 30 min slots with current set up
- no earlier than 6 am and stop at 12am
	- can justify as a family restriction/assumption (could be a part of config steps)
- additional individual calendars -> should we even demo an individual calendar?
	- ask Rosti
## Presentation
- going well
- 7 assessed points that need to be discussed
- time limit means that there would only be 30 sec per point, so will use a different structure
- slides and practice continuing by Ali & Alex
- want to name drop as much technical jargon as possible in presentation
## Database schema progress
- querying with no SQL might be more difficult
- <Lucas' diagram>
- Hash events by time slot?
	- still a unique identifier
	- update database rather than create table each time
- still not confirmed no sql -> Lucas will continue to investigate and ensure they can work with the microcontrollers
- might be worth using sql and have a more difficult set up at the beginning if it means it will make usage and integration easier
- if we have a laptop going for a display, may as well run a database engine on that
- use http on local host to post/get
- Lucas can create library/API
	- could use requests library
## Display progress
- HDMI 26" screen
- Make sure sketches/designs will be possible to display on computer over HDMI
- Need to look at screens able to be rented from department
	- otherwise, Ali is happy to buy a screen for herself and we can use over the semester
---
