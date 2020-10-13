# Dockerized Thought-App with Django and PostgreSQL

### Development

Uses the default Django development server.

1. *.env.dev* Configuration settings for Development(Debug on, localhost)
1. docker-compose.yml docker file for development(mounted app volume)
1. Build the images and run the containers:

    ```sh
    $ docker-compose up -d --build
    ```

    Test it out at [http://localhost:8000](http://localhost:8000). The "app" folder is mounted into the container and your code changes apply automatically.

### Production

Uses gunicorn + nginx.

1. *.env.prod* and *.env.prod.db* are Production configuration files for Docker and Database settings
1. Build the images and run the containers:

    ```sh
    $ docker-compose -f docker-compose.prod.yml up -d --build
    ```

    Test it out at [http://localhost:1337](http://localhost:1337). No mounted folders.


### Loading Fixtures

Example on loading users fixtures from Django manage.py of the running container web-app
    
    
    $ docker-compose -f docker-compose.prod.yml exec web python manage.py loaddata fixtures/users.json


### Future Work

#### Adding Machine Learning(ML) sklearn docker support by changing Alpine base image

