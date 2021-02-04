# This target can be used to regenerate the main css file
# This can be used for a development environment in order to prevent re-compiling the whole carbon-design scss on every request
#
VENV := . .venv/bin/activate &&

quickstart: debian_packages create_venv pip_packages create_db create_superuser compile_scss

debian_packages:
	sudo apt update
	sudo apt install make python3-venv python3-dev

create_superuser:
	${VENV} echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell

pip_packages:
	${VENV} pip install -r requirements.txt

create_venv:
	python3 -m venv .venv

create_db:
	${VENV} python manage.py migrate

compile_scss:
	rm -rf static/CACHE/css
	${VENV} python manage.py compress -f
	touch basxconnect_demo/settings/local.py
	sed -i -e '/OVERRIDE_STYLESHEET/d' basxconnect_demo/settings/local.py
	echo OVERRIDE_STYLESHEET = '"'/static/CACHE/css/$$(\ls static/CACHE/css)'"' >> basxconnect_demo/settings/local.py

runserver:
	echo IP addresses
	ip addr | awk '/inet / {print $$2}'
	${VENV} python manage.py runserver 0.0.0.0:8000
