from fastapi import Body, APIRouter, HTTPException
from app.dependencies.database import cal_col, user_col
import time as time_lib
import app.utils as utils
from typing import Annotated

router = APIRouter(
    prefix="/whiteboard",
    tags=["Whiteboard"]
)


@router.post("/{user}")
def modify_calendar(user: str):
    users = user_col.distinct("user_id")
    users.append("family")
    print(users)
    if user not in users:
        raise HTTPException(status_code=400, detail="That user_id is not valid")
    return {"message": user}
