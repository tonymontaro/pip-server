# pipit
A tool for managing PIP process in Andela

# Installation
- Git clone the repository

Install all project dependencies by running the command below:
- Run pip install -r requirements.txt

- Create a postgres database and set the database
- Create a .envrc file and add required variables (example rc file is .envrc_sample)
- install direnv and export variables ``brew install direnv`` and ``direnv allow``
- Run python manage.py db upgrade

For subsequent changes to models, simply run ``python manage.py db migrate`` to generate the migration and then ``python manage.py db upgrade`` to apply the migration to the database


# Testing
- Run ``python manage.py test``
