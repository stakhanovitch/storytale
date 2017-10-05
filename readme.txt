

#////////////////////////
#DB CONFIG
#////////////////////////

CREATE DATABASE myproject;
CREATE USER myprojectuser WITH PASSWORD 'password';

ALTER ROLE myprojectuser SET client_encoding TO 'utf8';
ALTER ROLE myprojectuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myprojectuser SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;



#////////////////////////
#Python config
#////////////////////////

# package for psql db
pip install django psycopg2

#move to project directory
Python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser




TIPS:
pour le menu : 
#rename url as smth
{%url 'home' as home %}
{% if request.path == home %} do smth

contact form :
https://youtu.be/9Wbfk16jEOk?t=1h45m12s