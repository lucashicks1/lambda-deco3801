from fastapi import FastAPI
from app.routers import figures_router

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

@app.get("/")
async def root():
    return {"message": "Dylan loves deco"}