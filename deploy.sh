#!/bin/sh
olddir=$(pwd)
cd $(dirname $(realpath $0))

git pull
. .venv/bin/activate

pip install --upgrade -r requirements.txt
./manage.py migrate
./manage.py collectstatic --settings=basxconnect_demo.settings.production --noinput
./manage.py compress --settings=basxconnect_demo.settings.production --force

deactivate

cd $olddir
