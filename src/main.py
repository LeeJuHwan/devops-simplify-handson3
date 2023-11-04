# pip install uvicorn
# pip install "fastapi[all]"
# uvicorn src.main:app

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from typing import Dict

app = FastAPI(
    title="FastAPI - Hello World code",
    description="This is the Hello World of FastAPI.",
    version="1.0.0",
)


@app.get("/")
def hello_world():
    payload: Dict[str, str] = {"Hi": "World"}
    return JSONResponse(payload)
