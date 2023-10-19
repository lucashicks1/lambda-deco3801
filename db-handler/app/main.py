"""Fast api app that is run when api starts"""
import logging
from fastapi import FastAPI, HTTPException, responses
from fastapi.middleware.cors import CORSMiddleware
from app.routers import figures_router, whiteboard_router, display_router
from app.constants import LOGGER_FORMAT, LOGGER_TIME_FORMAT
from app.dependencies.database import cal_col
from app import utils

tags_metadata = [
    {
        "name": "Display",
        "description": "All endpoints used by the family display",
    },
    {
        "name": "Figurines",
        "description": "All endpoints used by the figurines display",
    },
    {
        "name": "Whiteboard",
        "description": "All endpoints used by the lambda board",
    },
]

origins = ["http://0.0.0.0:3000", "http://localhost:3000"]

app = FastAPI(title="Lambda DB Handler", openapi_tags=tags_metadata)

# Adds CORS middleware for react app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Includes all of the endpoint routers
app.include_router(figures_router.router)
app.include_router(whiteboard_router.router)
app.include_router(display_router.router)

logging.basicConfig(level=logging.INFO, format=LOGGER_FORMAT, datefmt=LOGGER_TIME_FORMAT)
_LOGGER = logging.getLogger(__name__)
logging.getLogger(__name__).setLevel(logging.DEBUG)


# Redirect main endpoint to the docs
@app.get("/", summary="Default landing page which will redirect you to the docs")
def main():
    """root endpoint of the API that redirects to the API docs"""
    # Redirects you to doc page
    return responses.RedirectResponse("/docs")


@app.get(
    "/dump",
    summary="Private endpoint that is used to quickly dump the database contents",
)
def dump():
    """Private endpoint solely used to dump the current contents of the database.
    Endpoint would not be public facing"""
    return {"body": list(cal_col.find({}, {"_id": 0}))}


@app.post("/reset", summary="Resets the state of the database")
def reset(reset: bool = False, populate: bool = True):
    """Resets the database if state is true

    Args:
        reset (bool, optional): Whether the database will be reset. Defaults to False.
        populate (bool, optional): Whether the database will be populated with random timeslots when reset
    """
    if reset:
        _LOGGER.info("Resetting database state")
        utils.reset_db(populate=populate)
        if populate:
            _LOGGER.info("Populating database")

        return {"body": list(cal_col.find({}, {"_id": 0}))}

    elif populate:
        raise HTTPException(
            status_code=400,
            detail="You cannot populate the database without resetting it.",
        )
    return None
