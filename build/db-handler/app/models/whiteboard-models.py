import typing

from pydantic import BaseModel
from typing import Literal, Optional
from app import constants


class TimeSlot(BaseModel):
    day: Literal[tuple[constants.DAYS]]
    timeslot: int
    data: Optional[str] = None