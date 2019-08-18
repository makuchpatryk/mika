#!/usr/bin/env bash

./manage.py collectstatic --clear --noinput
./manage.py compress
./manage.py collectstatic --noinput

./manage.py runserver