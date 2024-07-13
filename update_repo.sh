#!/bin/bash

# Check status
git status

# Add changes
git add .

# Commit changes with a message
git commit -m "$1"

# Push to the main branch
git push origin main
