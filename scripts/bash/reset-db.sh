#!/bin/bash

echo; echo "Resetting the database"; echo
rm -r frontend/migrations/
rm kedfilms/kedfilms.sqlite3
mkdir frontend/migrations/
touch frontend/migrations/__init__.py

echo; echo "Creating the database with South wrapper"; echo
./manage.py makemigrations
./manage.py syncdb
./manage.py migrate

echo; echo "Populating the database"; echo
./manage.py shell < scripts/database/populate.py

echo; echo "Everything is done! Launching the server..."; echo
./manage.py runserver


