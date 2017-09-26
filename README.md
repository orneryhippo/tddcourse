#README.md
This is based on http://testdriven.io/
In this version we will change the docker setup to be heroku-based

Instead of docker and docker-compose we will use heroku

Create a heroku account and download and install the heroku toolbelt for your os

open a commandline window

navigate to the dev directory and create the project directory, and switch to it
activate the virtualenvironment
(venv) $  pip install flask, flask-admin [, etc]

git init

create the files
create a .gitignore file [contents of .gitignore  excluding venv, __pycache__, *.pyc etc ]
create a Procfile [contents of Procfile] 
create a requirements.txt file using (venv) $ pip freeze > requirements.txt 
git add .
git commit -m"initial commit"
heroku login
provide username:
provide password at the prompts:
heroku create app_name
git push heroku master
"""
heroku addons:create heroku-postgresql --app app_name
"""
heroku addons -a app_name
heroku config
[note the DATABASE_URL has been created] 
"""
heroku run bash -a app_name
