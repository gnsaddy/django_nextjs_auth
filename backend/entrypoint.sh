#!/bin/sh

echo "**************** waiting for server volume ****************"
until cd /app/backend
do
    echo "**************** Waiting for server volume ****************"
done

echo "**************** Waiting for db to be ready ****************"

echo "**************** migrating ****************"
python ./manage.py migrate

echo "**************** running migrations ****************"
python ./manage.py makemigrations

python ./manage.py migrate

echo "**************** collecting static ****************"
python ./manage.py collectstatic --noinput 

echo "**************** starting gunicorn ****************"
gunicorn --bind 0.0.0.0:8003 backend.wsgi --workers 2 --threads 4 --log-level debug --reload
echo "**************** gunicorn running ****************"