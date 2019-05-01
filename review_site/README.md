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