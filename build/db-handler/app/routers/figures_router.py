from fastapi import APIRouter
from app.dependencies.database import cal_col
from datetime import datetime
import time as time_lib

router = APIRouter(
    prefix="/figurines",
    tags=["figurines"]
)

@router.get("")
async def get_available():
    time: str = time_lib.strftime("%H")
    return {"message": time}