#!/bin/bash


echo "Starting"
python3 manage.py migrate &&
python3 manage.py collectstatic --noinput &&
python3 manage.py runserver 0.0.0.0:8000 &
python3 bot.py
echo "Stop"

exit $?