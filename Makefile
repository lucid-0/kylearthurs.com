migrations:
	docker run kylearthurs python /app/kylearthurs/manage.py makemigrations --settings=kylearthurs.settings_docker

dev-admin:
	docker run -it kylearthurs python /app/kylearthurs/manage.py createsuperuser --username=admin --email=admin@example.com --settings=kylearthurs.settings_docker