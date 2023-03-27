# School registering System API made with DRF :snake:

### This project is still in development! Some new features will be added in the coming days and the documentarion will be optimized :warning:

## Used technologies:

* Python
* Django
* Django Rest Framework

## How to set up the enviroment:


1. Type in the terminal `python -m venv venv`.
2. Type `source venv/bin/activate` (For linux users) or `venv/Scritps/activate` (For Windows users).
3. Type `pip install -r requirements.txt`.
4. Create a **.env** file and add the SECRET_KEY enviroment variable(With no '' or "").
5. Type `python manage.py migrate` to run the models migrations.
6. Type `python manage.py createsuperuser` and follow the steps.
7. Type `python manage.py runserver` and there you go! The API server is running

## How can i test the API?

### The only thing you need to do is go in the `localhost:8000/` endpoint.
