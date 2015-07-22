#!/bin/bash

echo; echo "Resetting..."; echo
rm -r sqlite3app/migrations/
rm loveinjection/supersecure.sqlite3
mkdir sqlite3app/migrations/
touch sqlite3app/migrations/__init__.py

echo; echo "Creating..."; echo
./manage.py makemigrations
./manage.py syncdb
./manage.py migrate

echo; echo "Populating..."; echo
./manage.py shell < scripts/database/populate.py

echo; echo "Launching the server..."; echo
./manage.py runserver


