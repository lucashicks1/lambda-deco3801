from uuid import uuid4

from fastapi import FastAPI
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

@app.get("/")
async def test():
    test_dict = {"name": str(uuid4())}
    cal_col.insert_one(test_dict)
    return {"message": "Dylan loves deco!!!"}
