from uuid import uuid4

from fastapi import FastAPI, responses
from app.routers import figures_router
from app.dependencies.database import cal_col

tags_metadata = [
    {
        "name": "Figure Display Endpoints",
        "description": "All endpoints will be used by the figurine display"
    }
]

app = FastAPI(
    title="Lambda DB Handler",
    openapi_tags=tags_metadata
)

app.include_router(figures_router.router)


@app.get("/", summary="Default landing page which will redirect you to the docs")
async def main():
    # Redirects you to doc page
    return responses.RedirectResponse("/docs")