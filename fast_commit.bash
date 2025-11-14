#!/bin/bash

files=$(git ls-files --others --exclude-standard)
lines="$(echo "$files" | wc -l)"

if [ "$lines" -lt 1 ]; then
    echo "Unable to commit, no changes detected"
    exit 1
elif [ "$lines" -gt 1 ]; then
    echo "Unable to auto-commit, more than 1 file detected"
    exit 2
fi

green=$(tput setaf 2)   # Green
red=$(tput setaf 1)     # Red
reset=$(tput sgr0)

echo
echo "${green}Executing 'git add .'${reset}"
git add .

echo
echo "${green}Executing 'git commit -m \"Added $files\"'${reset}"
git commit -m "$files"

echo
echo "${green}Executing 'git push'${reset}"
git push