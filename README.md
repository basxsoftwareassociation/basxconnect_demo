About
=====

This is a demo application of the basxConnect CRM system.

The goal of this CRM is to support charities.

This effort is made possible by the basx Software Association and its partners.

Installation
============

Have a look at https://get.basxconnect.solidcharity.com/

Or do these manual steps:

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
