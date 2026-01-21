#!/usr/bin/env bash
# exit on error
set -o errexit

# Installer les dépendances
pip install -r requirements.txt

# Collecter les fichiers statiques (CSS/JS)
python manage.py collectstatic --no-input

# Appliquer les migrations de la base de données
python manage.py migrate


python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'yedjenounadia@gmail.com', 'admin1234') if not User.objects.filter(username='admin').exists() else None"