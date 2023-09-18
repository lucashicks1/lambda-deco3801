from fastapi import Body, APIRouter, Query
from app.dependencies.database import cal_col, user_col
import time as time_lib
from app import utils, constants
from typing import Annotated

from app.models.item_model import Item, openapi_examples

router = APIRouter(
    prefix="/display",
    tags=["Display"]
)


@router.get("/user-free-timeslots",
            summary="Gets the timeslots that have a certain number of free users. Each slot is sorted in descending "
                    "order in terms of how many people are free during it")
async def get_free_timeslots(
        min_num_users: Annotated[
            int, Query(
                title="The minimum number of available users",
                ge=0,
                le=user_col.count_documents({"user_id": {"$ne": constants.FAMILY_NAME}}))] = 0) -> \
        Annotated[
            dict, Body(
                openapi_examples={
                    "normal": {
                        "summary": "A normal example",
                        "description": "A **normal** item works correctly.",
                        "value": {
                            "name": "Foo",
                            "description": "A very nice Item",
                            "price": 35.4,
                            "tax": 3.2,
                        },
                    },
                    "converted": {
                        "summary": "An example with converted data",
                        "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                        "value": {
                            "name": "Bar",
                            "price": "35.4",
                        },
                    },
                    "invalid": {
                        "summary": "Invalid data is rejected with an error",
                        "value": {
                            "name": "Baz",
                            "price": "thirty five point four",
                        },
                    },
                },
            )]:
    num_users: int = user_col.count_documents({"user_id": {"$ne": constants.FAMILY_NAME}})
    print(f"NUM USERS {num_users}")
    num_booked_users: int = num_users - min_num_users
    print(min_num_users)
    query: list = [
        {
            "$match": {
                "booked_users": {"$exists": True},
                "$expr": {
                    "$lte": [{"$size": "$booked_users"}, num_booked_users]
                }
            }
        },
        {
            "$addFields": {
                "test": {
                    "$map": {
                        "input": "$booked_users",
                        "in": {"$subtract": [num_users - 1, {"$size": "$booked_users"}]}
                    }
                },
                "num_free_users": {"$subtract": [num_users - 1, {"$size": "$booked_users"}]}
            }
        },
        {
            "$sort": {
                "num_free_users": 1
            }
        },
        {
            "$project": {
                "_id": 0
            }
        }
    ]
    print(f"Less than or equal to {num_booked_users}")
    return {"body": list(cal_col.aggregate(query))}


@router.get("", summary="Gets map of all users and their availability for that timeslot")
async def get_available() -> Annotated[dict, Body(
    examples=[
        {
            "user_1": 1,
            "user_2": 0,
            "user_3": 1,
            "user_4": 0
        }
    ]
)]:
    users: dict = {}
    timeslot: str = utils.current_to_timeslot()
    booked_users = cal_col.find_one({"day": time_lib.strftime("%A").lower(), "time": timeslot}).get("booked_users")
    for user in user_col.distinct("user_id"):
        status = 1 if user in booked_users else 0
        users[user] = status
    return users


