import datetime
from os import environ
import uvicorn
from fastapi import FastAPI, File, UploadFile
import cv2
import numpy as np

app = FastAPI()


@app.get("/date")
async def get_date():
    return {"date": str(datetime.datetime.now())}

@app.post("/faces/")
async def count_faces(file: UploadFile = File(...)):
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml")
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=3, minSize=(30, 30))
    return {"numm_faces": len(faces)}

if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=int(environ.get("PORT", 5000)))
