from fastapi import FastAPI, responses
from app.routers import figures_router, whiteboard_router, display_router
from app.dependencies.database import cal_col
from app import help_scripts

tags_metadata = [
    {
        "name": "Display",
        "description": "All endpoints used by the family display"
    },
    {
        "name": "Figurines",
        "description": "All endpoints used by the figurines display"
    },
    {
        "name": "Whiteboard",
        "description": "All endpoints used by the lambda board"
    }
]

app = FastAPI(
    title="Lambda DB Handler",
    openapi_tags=tags_metadata
)

app.include_router(figures_router.router)
app.include_router(whiteboard_router.router)
app.include_router(display_router.router)


@app.get("/", summary="Default landing page which will redirect you to the docs")
async def main():
    # Redirects you to doc page
    return responses.RedirectResponse("/docs")


@app.get("/reset", summary="Resets the state of the database")
async def reset(reset: bool = False):
    if reset:
        help_scripts.reset_db()

@app.get("/dump", summary="DUMPS THE MONGODB FOR TESTING")
async def dump():
    return {"body": list(cal_col.find({}, {"_id": 0}))}
