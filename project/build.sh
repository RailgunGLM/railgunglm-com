#!/bin/bash

# Update pip
echo "Updating pip..."
python3.10 pip install -U pip

# Install dependencies

echo "Installing project dependencies..."
python3.10 -m pip install -r requirements.txt

# Make migrations
echo "Making migrations..."
python3.10 manage.py makemigrations --noinput
python3.10 manage.py migrate --noinput

# Collect staticfiles
echo "Collect static..."
python3.10 manage.py collectstatic --noinput --clear

echo "Build process completed!"
