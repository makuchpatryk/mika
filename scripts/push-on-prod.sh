#!/usr/bin/env bash
ssh makuchpatryk.xyz << "EOF"
cd /home/patryk/project/mika
git pull origin master
source ../env/mika/bin/activate
./manage.py collectstatic --clear --noinput
./manage.py collectstatic --noinput
sudo service uwsgi restart
EOF