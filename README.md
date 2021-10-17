# django-graphql-cookiecutter
A Django, GraphQL, Relay cookiecutter.

## Environment and Package Management
Install Poetry

    $ pip install poetry
    
Activate or Create Env    

    $ poetry shell
    
Install Packages from Poetry
  
    $ poetry install
    
Install New Package
  
    $ poetry add <pip package-name>    
    
## Migrate Data

    $ ./manage.py migrate
   
## Start Server

    $ python manage.py runserver

The app will be served by django **runserver**

Access it through **http://127.0.0.1:8000**
  
## Run Celery Tasks   

    $ celery -A backend worker --loglevel=info -E --concurrency=10

## Export Requirements  

    $  poetry export -f requirements.txt --output requirements.txt


## Version
* Python: 3.8+
* PostgreSQL: 12+
* Redis: 3.5+
