# Ridgefield-Farm-Database
A Django Project created for UWA Ridgefield Farm written in Python, Javascript, HTML and CSS.

## Usage
This Django Project can be run locally.
First start by downloading from the requirements.txt file into a Virtual Environment.
Then run the following command in that environment (in the same directory as 'manage.py'):
```sh
python manage.py runserver
```
You may want to create a superuser to log in
```sh
python manage.py createsuperuser
```
Can refer to this artile from Geeks4Geeks for more:
https://www.geeksforgeeks.org/how-to-create-superuser-in-django/

### You will also need to create a database file 'db.sqlite3', as it was removed for safety reasons

## Deployment
The site is currently deployed using Heroku, hence the Procfile.
