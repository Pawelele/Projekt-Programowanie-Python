FROM python:3.10-slim

WORKDIR api
COPY . .

RUN pip3 install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]