## django_blog - A mini blog

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]() 
  [![GitHub Issues](https://img.shields.io/github/issues/kevinbowen777/django_blog.svg)](https://github.com/kevinbowen777/django_blog/issues)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

django_blog is a demonstration of basic Django functionality.

### Installation
 - `git clone https://github.com/kevinbowen777/django_blog.git`
 - `cd django_start`
 - Local installation:
     - `poetry shell`
     - `poetry install`
     - `python manage.py migrate`
     - `python manage.py createsuperuser`
     - `python manage.py runserver`
 - Docker installation:
     - `docker-compose up --build`
     - `docker-compose python manage.py migrate`
     - `docker-compose python manage.py createsuperuser`
 - Browse to http://127.0.0.1:8000 or http://127.0.0.1:8000/admin/

---
## Features
 - User registration
 - Create, edit, and delete posts
 - Admin management of users and posts

### Live Demo on Heroku:
 - [django_blog](https://kbowen-django-blog.herokuapp.com/)
### Docker Container Image:

 - N/A
---
## Screenshots

### Home
![Home](https://github.com/kevinbowen777/django_blog/blob/master/images/django_blog_homepage.png)

---
### Reporting Bugs

   Visit the [Issues page](https://github.com/kevinbowen777/django_blog/issues)
      to view currently open bug reports or open a new issue.
