#!/bin/bash

# 1. Check if archive directory exists, create if not
if [ ! -d "archive" ]; then
    mkdir -p archive
    echo "Created 'archive' directory."
fi

# 2. Check if grades.csv exists
if [ ! -f "grades.csv" ]; then
    echo "Error: grades.csv does not exist to archive."
    exit 1
fi

# 3. Generate timestamp and archive grades.csv
TIMESTAMP=$(date +"%Y%m%d-%H%M%S")
ARCHIVED_NAME="grades_${TIMESTAMP}.csv"
cp grades.csv "archive/$ARCHIVED_NAME"
echo "Archived grades.csv to archive/$ARCHIVED_NAME"

# 4. Reset workspace with a fresh grades.csv template
cat <<EOL > grades.csv
assignment,group,score,weight
Quiz,Formative,0,20
Group Exercise,Formative,0,20
Functions and Debugging Lab,Formative,0,20
Midterm Project - Simple Calculator,Summative,0,20
Final Project - Text-Based Game,Summative,0,20
EOL
echo "Created a fresh grades.csv template in the workspace."

# 5. Log the action into organizer.log
LOG_ENTRY="[$(date +"%Y-%m-%d %H:%M:%S")] Archived grades.csv to archive/$ARCHIVED_NAME"
echo "$LOG_ENTRY" >> organizer.log
echo "Logged action to organizer.log."
