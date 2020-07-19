# Mani Django Template

Template for future projects built with 
[![Python Version](https://img.shields.io/badge/python-3.7-hotpink.svg)](python.org/dev/peps/pep-0537/)
[![Django Version](https://img.shields.io/badge/django-3.0-hotpink.svg)](https://djangoproject.com)


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Installing

A step by step series of examples that tell you how to get a development env running

Git clone

```
Git URL will go here
```

Install the requirements 

```
pip install -r requirements.txt
```

Switch the Database in Settings.py of the project
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Setup the migrations

```
python manage.py makemigrations
```

Make the migrations

```
python manage.py migrate
```

Create Super User

```
python manage.py createsuperuser
```

Run Server

```
python manage.py runserver
```

End with an example of getting some data out of the system or using it for a little demo

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

