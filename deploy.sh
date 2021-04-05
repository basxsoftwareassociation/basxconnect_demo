#!/bin/sh
olddir=$(pwd)
cd $(dirname $(realpath $0))

git pull
. .venv/bin/activate

pip install --upgrade -r requirements.txt
./manage.py migrate
./manage.py collectstatic --noinput
./manage.py compress --force

deactivate

cd $olddir
