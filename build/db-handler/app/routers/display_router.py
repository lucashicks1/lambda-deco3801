from fastapi import Body, APIRouter, Query
from app.dependencies.database import cal_col, user_col
from app import constants
from typing import Annotated
from app.examples.display_payloads import *

router = APIRouter(
    prefix="/display",
    tags=["Display"]
)


@router.get("/user-totals", summary="Calculates the total number of booked hours for each user.")
async def get_user_hours() -> Annotated[dict, Body(examples=[USER_TOTALS_EXAMPLES])]:
    # Find all users that aren't the family user
    users: list[str] = user_col.distinct("user_id", {"user_id": {"$ne": constants.FAMILY_NAME}})
    totals: dict[str, float] = {}

    # Count hours up for each timeslot
    for user in users:
        count = cal_col.count_documents({"booked_users": {"$in": [user]}})
        totals[user] = count * constants.TIMESLOT_LEN / 60

    return totals


@router.get("/family-timeslots", summary="Gets all of the timeslots that the family has booked in time for.")
async def get_family_timeslots() -> Annotated[dict, Body(examples=[FAMILY_TIMESLOTS_EXAMPLE])]:
    documents: list = list(cal_col.find({"booked_users": {"$in": [constants.FAMILY_NAME]}}, {"_id": 0}))
    return {"body": documents}


@router.get("/user-free-timeslots",
            summary="Gets the timeslots that have a certain number of free users. Each slot is sorted in descending "
                    "order in terms of how many people are free during it")
async def get_free_timeslots(
        min_num_users: Annotated[
            int, Query(
                title="The minimum number of available users",
                ge=0,
                le=user_col.count_documents({"user_id": {"$ne": constants.FAMILY_NAME}}))]
        = user_col.count_documents({"user_id": {"$ne": constants.FAMILY_NAME}})) -> Annotated[
    dict, Body(examples=[FREE_TIMESLOTS_EXAMPLE])]:
    num_users: int = user_col.count_documents({"user_id": {"$ne": constants.FAMILY_NAME}})
    num_booked_users: int = num_users - min_num_users

    # Aggregation pipeline to find the timeslots with correct number of free users
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
                "num_free_users": {"$subtract": [num_users, {"$size": "$booked_users"}]}
            }
        },
        {
            "$sort": {
                "num_free_users": -1
            }
        },
        {
            "$project": {
                "_id": 0
            }
        }
    ]
    return {"body": list(cal_col.aggregate(query))}
