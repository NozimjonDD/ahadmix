#!/bin/bash

python manage.py makemigrations
python manage.py migrate

echo -e "\e[32m✅ Successful\e[0m"