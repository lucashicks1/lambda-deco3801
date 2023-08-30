from fastapi import FastAPI
from app.dependencies.database import cal_col
from uuid import uuid4

app = FastAPI()

test_dict = {"name": str(uuid4())}

@app.get("/")
async def test():
    cal_col.insert_one(test_dict)
    return {"message": "Dylan loves deco!!!"}
