from pydantic import BaseModel
from typing import Literal, Optional, List
from app import constants


# Pydantic model used to validate each timeslot passed into the whiteboard endpoints
class TimeSlot(BaseModel):
    day: Literal[tuple(constants.DAYS)]
    time_slot: int
    data: Optional[str] = None
    color: Optional[str] = None


# Request payload passed into whiteboard routers
class WhiteboardRequest(BaseModel):
    body: List[TimeSlot]
