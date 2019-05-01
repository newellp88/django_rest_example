# Django REST API
Simple API that allows users to create
accounts, get an authentication token,
post new company reviews, and get a list
of reviews they've posted

### Project Setup
Assuming Ubuntu 18.04 and Python3.6.7 are installed:
```
mkdir django_rest_example
python3 -m venv django_rest_example/
cd django_rest_example/
source bin/activate
pip install django djangorestframework django-coreapi
django-admin startproject review_site
cd review_site/
python manage.py startapp api
```
With the project framework setup, we can get started with the db and code.

### Database Setup
Using MySQL for this project, to install on Ubuntu 18.04 from terminal:

```
# installation
sudo apt update
sudo apt install mysql-server
sudo mysql_secure_installation

# initial login
sudo mysql

# create new user; change 'peter' and 'password' and keep them somewhere safe
mysql > CREATE USER 'peter'@'localhost' IDENTIFIED BY 'password';
mysql > GRANT ALL PRIVELEGES ON *.* TO 'peter'@'localhost' WITH GRANT OPTION;

# create our database while we're here
mysql > CREATE DATABASE review_site;
mysql > exit
```
Now that the database is setup, install the mysqlclient driver:
```
sudo apt-get install default-libmysqlclient-dev
pip install mysqlclient
```

### Running this project
- Git clone this repo
- Follow the setup instructions above, `pip install -r requirements.txt` will
install the pip packages named
- Initalize the database:
```
python manage.py makemigrations
python manage.py migrate
```
- Run the server: 
```
python manage.py runserver
```
- Navigate to `localhost:8000/api/v1/users` and create a user
- Copy the token response from user creation, the token needs
to be added into `api/tests.py` and replace the current token.
- Run the tests `python manage.py test`
- Create a superuser to view the admin panel: 
`python manage.py createsuperuser --username admin --email admin@test.com` and choose a password
- Use your favorite package to send authorized requests to 
`/api/v1/reviews` to create and view your posts. Example:
```
import json
import requests

url = "http://127.0.0.1:8000/api/v1/reviews"
auth = "Token %s" % "c843a4eba7e96a47734da0f80daf1e8f10e3524b"
headers = {"Authorization": auth, "content-type": "application/json"}
review = {"rating": 4, "title": "Chipotle is pretty nifty", "summary": "they have guac", "company": "Chipotle"}

# create a new review
r= requests.post(url, headers=headers, data=json.dumps(review))

# get a list of your reviews
r = requests.get(url, headers=headers)
print(json.loads(r.content))
```
- Visit `/docs` for details about available endpoints, functions and parameters