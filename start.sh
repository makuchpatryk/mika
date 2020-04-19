#!/usr/bin/env bash

if [ "$1" = "sass" ]
then
    echo "I am compiling, please wait"
    node node_modules/gulp/bin/gulp.js sass --production
fi

./manage.py collectstatic --clear --noinput
./manage.py compress
./manage.py collectstatic --noinput

./manage.py runserver