#!/bin/bash
git clone https://github.com/ABDULMAJEED7778/Library-Management-System.git
cd Library-Management-System
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
