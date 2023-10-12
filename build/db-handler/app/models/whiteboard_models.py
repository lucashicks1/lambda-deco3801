"""Models outlining the payloads required for the whiteboard endpoint"""
from typing import Literal, Optional, List
from pydantic import BaseModel
from app import constants


class TimeSlot(BaseModel):
    """Pydantic model used to validate each timeslot passed into the whiteboard endpoints"""

    # Ignore pylance warning message
    day: Literal[tuple(constants.DAYS)]
    time_slot: int
    data: Optional[str] = None
    colour: Optional[str] = None


# Request payload passed into whiteboard routers
class WhiteboardRequest(BaseModel):
    """Pydantic model used to validate payload passed into whiteboard endpoints"""

    body: List[TimeSlot]
