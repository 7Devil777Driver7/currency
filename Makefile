SHELL := /bin/bash

manage_py := python app/manage.py


runserver:
	$(manage_py) runserver 0:8000

migrate:
	$(manage_py) migrate

makemigrations:
	$(manage_py) makemigrations

shell:
	$(manage_py) shell_plus --print-sql

show_urls:
	$(manage_py) show_urls

createsuperuser:
	$(manage_py) createsuperuser
