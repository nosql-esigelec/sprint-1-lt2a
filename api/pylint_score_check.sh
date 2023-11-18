#!/bin/bash
# Run pylint and capture its output
output=$(python3.9 -m pylint $@)

# Extract the score from the output
score=$(echo "$output" | grep "Your code has been rated at" | awk '{print $7}' | cut -d'/' -f1)

# Check if the score is 7.0 or higher
if (( $(echo "$score >= 7.0" | bc -l) )); then
    exit 0
else
    echo "Your Pylint score is $score which is below 7.0"
    exit 1
fi