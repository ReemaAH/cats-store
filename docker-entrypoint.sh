#!/bin/sh

# Apply database migrations
echo "Apply database migrations"
env/bin/python manage.py migrate

# Start server
echo "Starting server"
# python manage.py runserver 0.0.0.0:8000
env/bin/python manage.py runserver 0.0.0.0:8000
