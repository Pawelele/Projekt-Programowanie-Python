import uvicorn
from fastapi import FastAPI, File, UploadFile
import datetime
import cv2
import numpy as np
from fastapi.responses import StreamingResponse
import io
from os import environ

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

# @app.post("/betterFaces/")
# async def count_faces(file: UploadFile = File(...)):
#     contents = await file.read()
#
#     f_cascade = cv2.CascadeClassifier("face.xml")
#     e_cascade = cv2.CascadeClassifier("eye.xml")
#
#     nparr = np.frombuffer(contents, np.uint8)
#     img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#     faces = f_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
#     for (x, y, w, h) in faces:
#         cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
#         roi_gray = gray[y:y + h, x:x + w]
#         roi_color = img[y:y + h, x:x + w]
#         eyes = e_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=3, minSize=(10, 10))
#         for (ex, ey, ew, eh) in eyes:
#             cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
#
#     success, buffer = cv2.imencode('.jpg', img)
#     if not success:
#         raise Exception("Failed to encode image")
#
#     return StreamingResponse(io.BytesIO(buffer), media_type="image/jpeg")
if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=int(environ.get("PORT", 5000)))