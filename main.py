# main.py

from fastapi import FastAPI
from f1_data import getLapTimes

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/lapdata/{year}/{race}")
async def root(year,race):
        return getLapTimes(year,race,"R")