# pipit
A tool for managing PIP process in Andela

# Installation
- Git clone the repository

Install all project dependencies by running the command below:
- Run pip install -r requirements.txt

Create a postgres database and set the database URI as the value of ``DATABASE_URI`` and ``environment`` in your machine environment e.g export DATABASE_URL="postgresql://localhost/pip_server".
- Run python manage.py db upgrade

For subsequent changes to models, simply run ``python manage.py db migrate`` to generate the migration and then ``python manage.py db upgrade`` to apply the migration to the database
