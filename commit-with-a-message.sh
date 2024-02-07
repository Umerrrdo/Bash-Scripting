#!/bin/bash

# Move to the repository directory
cd ~/Documents/Github/Bash-Scripting

# Stage all changes
git add .

# Read a custom commit message from the user
echo -n "Enter your commit message: "
read commit_message

# Commit with the custom message
git commit -m "$commit_message"

# Push to the main branch
git push origin main
