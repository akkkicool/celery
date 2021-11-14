# Celery Django Project


## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all the required packages.

```bash
pip install -r requirements.txt
```
## Dependence
Install redis server in you machine.

## Start Celery

```bash
celery -A test_celery worker --beat -S django -l info
```
## Start Django application
```bash
python manage.py runserver
```
