#!/usr/bin/env bash

run_app () {
  if [[ -f "db.sqlite3" ]]; then
    python manage.py flush --no-input
  fi
  python manage.py migrate --no-input
  python manage.py createsuperuser --no-input
  python manage.py runserver 0.0.0.0:8000
}

run_app
