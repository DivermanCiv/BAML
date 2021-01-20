#!/bin/bash
# A simple django project deployment script for jenkins

BUILD_ROOT="/var/lib/jenkins/workspace/test/"
MNGR="/var/lib/jenkins/worskspace/test/manage.py"

echo "Sourcing python env..."
source "var/lib/jenkins/workspace/test/BAMLenv/bin/activate"

pip install -r requirements.txt

echo "Migrate model..."
python ${MNGR} makemigrations
python ${MNGR} migrate

echo "Collecting static files..."
python ${MNGR} collectstatic --noinput

# restart apache - deploy Django project
#echo "Restarting Apache server..."
#sudo apachectl graceful


echo "Run tests..."
python ${MNGR} jenkins #--enable-coverage
