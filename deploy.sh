#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run migrations
flask db upgrade

# Start the application
gunicorn -b 0.0.0.0:10000 myapp:app
