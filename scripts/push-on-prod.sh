#!/usr/bin/env bash
ssh makuchpatryk.xyz << "EOF"
cd /home/patryk/project/mika
git pull origin master
sudo service uwsgi restart
EOF