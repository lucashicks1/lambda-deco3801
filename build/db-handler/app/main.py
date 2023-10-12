from fastapi import FastAPI, responses
from fastapi.middleware.cors import CORSMiddleware
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

origins = [
    "http://0.0.0.0:3000",
    "http://localhost:3000"
]

app = FastAPI(
    title="Lambda DB Handler",
    openapi_tags=tags_metadata
)

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


# Redirect main endpoint to the docs
@app.get("/", summary="Default landing page which will redirect you to the docs")
async def main():
    # Redirects you to doc page
    return responses.RedirectResponse("/docs")


@app.get("/reset", summary="Resets the state of the database")
async def reset(state: bool = False):
    if state:
        help_scripts.reset_db()
