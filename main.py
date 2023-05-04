import uvicorn
from fastapi import FastAPI
import datetime

app = FastAPI()


@app.get("/date")
async def get_date():
    return {"date": str(datetime.datetime.now())}


