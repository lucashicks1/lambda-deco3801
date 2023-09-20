import typing

from pydantic import BaseModel
from typing import Literal, Optional, List
from app import constants


class TimeSlot(BaseModel):
    day: Literal[tuple(constants.DAYS)]
    time_slot: int
    data: Optional[str] = None
class WhiteboardRequest(BaseModel):
    body: List[TimeSlot]