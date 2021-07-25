# Teacher


### Features

1. Read and upload teachers from CSV file
2. Filter Teachers with their last names


# Development

Following are instructions on setting up your development environment.

The recommended way for running the project locally and for development is using Docker.


## Docker Setup

This project is set up to run using [Docker Compose](https://docs.docker.com/compose/) by default. It is the recommended way. You can also use existing Docker Compose files as basis for custom deployment

1. Install Docker:
   - Linux - [get.docker.com](https://get.docker.com/)
   - Windows or MacOS - [Docker Desktop](https://www.docker.com/products/docker-desktop)
1. Clone this repo 
1. Make sure `Pipfile.lock` exists. If it doesn't, generate it with:
   ```sh
   $ docker run -it --rm -v "$PWD":/django -w /django python:3.7 pip3 install --no-cache-dir -q pipenv && pipenv lock
   ```
1. Start up the containers:

   ```sh
   $ docker-compose up
   ```
1. populate the Postgres DB (in a separate terminal):
   ```sh
   $ docker-compose exec web python3 manage.py makemigrations
   $ docker-compose exec web python3 manage.py migrate
   ```
1. Create a superuser if required:
   ```sh
   $ docker-compose exec web python3 manage.py createsuperuser
   ```

