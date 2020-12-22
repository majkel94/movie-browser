#!/usr/bin/env bash

run_app () {
  python manage.py flush --no-input
  python manage.py migrate --no-input
  python manage.py createsuperuser --no-input
  python manage.py runserver 0.0.0.0:8000
}

run_app
