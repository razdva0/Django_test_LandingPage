#!/bin/bash
pip install -r requirements.txt
cd landingPage
python manage.py migrate
python manage.py runserver