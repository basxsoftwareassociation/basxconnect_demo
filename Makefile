# This target can be used to regenerate the main css file
# This can be used for a development environment in order to prevent re-compiling the whole carbon-design scss on every request
compile_scss:
	rm -rf static/CACHE/css
	. .venv/bin/activate && ./manage.py compress -f
	sed -i -e '/OVERRIDE_STYLESHEET/d' basxconnect_peacewatch/settings/local.py
	echo OVERRIDE_STYLESHEET = '"'/static/CACHE/css/$$(\ls static/CACHE/css)'"' >> basxconnect_peacewatch/settings/local.py
