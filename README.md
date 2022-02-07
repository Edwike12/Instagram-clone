#  project name:
INSTAGAM-CLONE myinsta app


# AUTHOR
EDWIKE NYAUNCHO


## Project description
This is a website created to clone popular photo app Instagram.


## USER STORY
-The user is able to sign in to the application to start using

-User is able to upload pictures to the application

-User can be able to see my profile with all pictures

-can also like a picture

-User is able to leave comment

-User is able to follow other users and see their pictures


## Setup Instructions and Installation
For the application to run, you have to install:

- python3.8

- Django framework

- virtual environment

- Postgres

Setup and Installation
- open terminal

- git clone this repository https://github.com/Edwike12/Instagram-clone

- use a code editor

- Actvate the virtual env 

        -$ source venv/bin/activate

- Install dependancies 

        -$ pip install -r requirements.txt

- Create a database

        -psql

        -CREATE DATABASE instagram;

- .env file- create  .env file and hve the following filling where appropriate:

            -SECRET_KEY = '<Secret_key>'

            -DBNAME = 'instagram'

            -USER = '<Username>'

            -PASSWORD = '<password>'

            -DEBUG = True

- Run initial migration

        -$ python3.8 manage.py makemigrations myinsta

        -$ python3.8 manage.py migrate

- Run the app

        -$ python3.8 manage.py runserver


## Technologies used
- python3.8

- Django

- Html, Css and Bootstrap

- postgres sql

- Heroku


## Known Bugs
There are no known bugs currently but pull requests are allowed incase you spot a bug


## Development 
Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:
- Fork the repo
- Create a new branch (git checkout -b improve-feature)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (git commit -am 'Improve feature')
- Push to the branch (git push origin improve-feature)
- Create a Pull Request


### Testing Application
-To run the tests for the class files:

    -$ python3.6 manage.py test




### contact information
Feel free to reach out:

Email: nyaunchoedwike@gmail.com




