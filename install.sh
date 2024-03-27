#!/bin/bash
git clone your_django_project_repo_url
cd your_django_project
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput