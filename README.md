# Face Detection API


This is a simple API for getting current date and detecting faces in images using FastAPI and OpenCV. The application has been containerized using Docker for easy deployment and management.

## Usage

### `/date`

Returns the current date and time.

GET
/date

#### Response

`date` (string): the current date and time in ISO format (YYYY-MM-DD HH:MM:SS.ssssss)

```
{
  "date": "2023-05-06 12:34:56.789012"
}
```



### `/faces`

Detects faces in an uploaded image.

POST 
/faces

Body:
{
  "file": photo.jpg
}

#### Response

`num_faces` (integer): the number of faces detected in the image

```
{
  "num_faces": 2
}
```


### Docker

To run the application using Docker, first build the image:

```
docker-compose build
```

Then start the container:

```
docker-compose up
```

This will start the API on `http://localhost:8080`.


## Deployment

### Requirements

- Docker

### Local deployment

1. Clone the repository:

```
git clone https://github.com/Pawelele/Projekt-Programowanie-Python.git
```

2. Move into the directory:

```
cd Projekt-Programowanie-Python
```

3. Build the Docker image:

```
docker-compose build
```

4. Start the Docker container:

```
docker-compose up
```

The API will be accessible at `http://localhost:8080`.


To stop the container run:

```
docker-compose stop
```

## Documentation

API endpoints documentation is available at http://localhost:8080/docs.
