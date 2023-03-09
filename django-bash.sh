#!/bin/sh

echo "Actualizando web..."

python manage.py flush
# PGPASSWORD=djangoproject psql --host db --port 5432 --username=code.djangoproject --dbname=code.djangoproject < tracdb/trac.sql
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic 
#python manage.py loaddata dev_sites
#python manage.py loaddata doc_releases
# git config --global url."https://".insteadOf git://
# python manage.py update_docs
#python manage.py loaddata dashboard_production_metrics
# python manage.py loaddata dashboard_example_data
#python manage.py update_metrics
#python manage.py update_index
#make compile-scss

exec "$@"