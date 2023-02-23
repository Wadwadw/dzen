#Dzen
This is a project for a commenting app built with Django and Docker.

Installation
To install the app, follow these steps:

1. Clone the repository:
    `git clone https://github.com/Wadwadw/dzen.git`
2. Change directory to the app:
   `cd dzen/comment_app`
3. Build the Docker containers:
    `docker-compose build`
4. Run the database migrations:
    `docker-compose run web python manage.py migrate`
5. Start the app:
    `docker-compose up`
6. Open the app in your browser:
    `http://localhost:9000`

#Usage
Once the app is running, you can use it to post comments, reply to comments, and filter main comments by name, email and add date.