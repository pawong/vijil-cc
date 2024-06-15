import json
import random
from uuid import uuid4

import uvicorn
from fastapi import APIRouter, FastAPI, Request

api = FastAPI()
router = APIRouter()


@api.get("/")
def read_root():
    return {"Hello": "World"}


@api.get("/alive")
def keep_alive():
    return "I'm alive!"


@api.get("/test-get/{num}")
def test_get(num: int):
    retval = []
    if num == 0:
        retval = [str(uuid4()) for _ in range(random.randint(1, 1000))]
    else:
        for _ in range(num):
            retval.append(str(uuid4()))
    return json.dumps({"retval": retval})


@api.post("/test-post")
async def test_post(request: Request):
    return await request.json()


@api.put("/test-put")
async def test_put(request: Request):
    return await request.json()


api.include_router(router)
