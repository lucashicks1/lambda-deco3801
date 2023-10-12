from typing import Annotated
from fastapi import Body, APIRouter, HTTPException
from app.dependencies.database import cal_col, user_col
from app.models.whiteboard_models import WhiteboardRequest
from app.examples.whiteboard_payloads import (
    POST_WHITEBOARD,
    RESPONSE_WHITEBOARD,
)

router = APIRouter(prefix='/whiteboard', tags=['Whiteboard'])


@router.post('/{user}')
def modify_calendar(
    user: str,
    payload: Annotated[WhiteboardRequest, Body(examples=[POST_WHITEBOARD])],
) -> Annotated[dict, Body(examples=[RESPONSE_WHITEBOARD])]:
    """Endpoint that updates the calendar with information given to the image capture software.

    Raises:
        HTTPException: 400 status code if the user provided is not valid

    Returns:
        dict: success message_description_
    """
    users = user_col.distinct('user_id')
    if user not in users:
        raise HTTPException(
            status_code=400, detail='That user_id is not valid'
        )

    # Deletes the user from the db timeslots
    cal_col.update_many({}, {'$pull': {'booked_users': user}})

    # Goes through each payload and updates the database
    for time_slot in payload.body:
        cal_col.update_one(
            {
                'day': time_slot.day,
                'slot_num': time_slot.time_slot,
                'data': time_slot.data,
            },
            {
                '$push': {
                    'booked_users': user,
                    'colour': time_slot.colour.split(','),
                }
            },
        )

    return {
        'body': list(
            cal_col.find({'booked_users': {'$in': [user]}}, {'_id': 0})
        )
    }
