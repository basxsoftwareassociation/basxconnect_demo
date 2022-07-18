About
=====

This is a demo application of the basxConnect CRM system.

The goal of this CRM is to support charities.

This effort is made possible by the basx Software Association and its partners.

Installation
============

Have a look at https://get.basxconnect.solidcharity.com/

Or do the following steps for a quick development setup:

for Fedora:

```
sudo dnf install git make
git clone https://github.com/basxsoftwareassociation/basxconnect_demo && cd basxconnect_demo
make quickstart_fedora
make runserver
```

for Debian:
```
sudo apt-get install git make
git clone https://github.com/basxsoftwareassociation/basxconnect_demo && cd basxconnect_demo
make quickstart_debian
make runserver
```

Now you can visit this link: http://127.0.0.1:8000/

