# This target can be used to regenerate the main css file
# This can be used for a development environment in order to prevent re-compiling the whole carbon-design scss on every request
#
VENV := . .venv/bin/activate &&
INSTANCE := basxconnect_demo

quickstart_debian: debian_packages quickstart

debian_packages:
	sudo apt update
	sudo apt install python3-venv python3-dev -y
	
quickstart_fedora: fedora_packages quickstart

fedora_packages:
	(rpm -qa | grep python3-devel) || sudo dnf install python3-devel

quickstart: create_venv pip_packages create_db create_superuser compile_scss build_searchindex
	@echo 
	@echo =====================================================================================
	@echo Installation has finished successfully
	@echo Run '"'make runserver'"' in order to start the server and access it through one of the following IP addresses
	@ip addr | sed 's/\/[0-9]*//' | awk '/inet / {print "http://" $$2 ":8000/"}'
	@echo Login user is '"'demo'"' password is '"'connectdemo'"'

create_venv:
	python3 -m venv .venv

pip_packages:
	${VENV} pip install -r requirements.txt

create_db:
	${VENV} python manage.py migrate
	${VENV} python manage.py compilemessages

create_superuser:
	${VENV} echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(is_superuser=True).exists() or User.objects.create_superuser('demo', 'demo@example.com', 'connectdemo')" | python manage.py shell

compile_scss:
	rm -rf static/CACHE/css
	${VENV} python manage.py collectstatic --noinput
	${VENV} python manage.py compress --settings basxconnect_demo.settings.production
	touch ${INSTANCE}/settings/local.py
	sed -i -e '/OVERRIDE_STYLESHEET/d' ${INSTANCE}/settings/local.py
	for i in $$(\ls static/CACHE/css); do cat static/CACHE/css/$$i >> static/CACHE/css/precompiled.css ; done
	echo OVERRIDE_STYLESHEET = '"'/static/CACHE/css/precompiled.css'"' >> ${INSTANCE}/settings/local.py

build_searchindex:
	${VENV} python manage.py rebuild_index --noinput


runserver:
	${VENV} python manage.py runserver 0.0.0.0:8000
