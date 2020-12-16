About
=====

This is a demo application of the basxConnect CRM system.

The goal of this CRM is to support charities.

This effort is made possible by the basx Software Association and its partners.

Installation
============

Have a look at https://get.basxconnect.solidcharity.com/

Or do these manual steps:

for Fedora:

```
dnf install perl-Image-ExifTool graphviz-devel python3-virtualenv python3-devel gcc git
```

for Debian:
```
apt-get install libimage-exiftool-perl libgraphviz-dev python3-virtualenv python3-venv python3-dev virtualenv gcc git pkg-config
```

Now get the code and setup the development environment:

```
git clone https://github.com/basxsoftwareassociation/basxconnect_demo.git
cd basxconnect_demo
virtualenv -p /usr/bin/python3 .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install black
python manage.py migrate
python manage.py createsuperuser
python manage.py compilemessages
python manage.py runserver
```

Now you can visit this link: http://127.0.0.1:8000/
