FROM python:3.10-slim

WORKDIR /app
COPY . .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

#CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "${PORT}"]
CMD ["python", "main.py"]
EXPOSE 5000