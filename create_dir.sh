#!/bin/bash

# Configuration
NUM_DIRS=25         # Number of directories to create
FILES_PER_DIR=2    # Number of files in each directory
BASE_DIR="2024"  # Base directory to hold all created directories
FILE_PREFIX="file" # Prefix for file names

# Create the base directory
mkdir -p "$BASE_DIR"

# Loop to create directories and files
for ((i=2; i<=NUM_DIRS; i++)); do
    DIR_PATH="$BASE_DIR/day_$i"
    
    echo "Created directory: $DIR_PATH"
    
    # Create files in the directory
    for ((j=1; j<=FILES_PER_DIR; j++)); do
        FILE_PATH="$DIR_PATH/solution.py"
        rm -f "$FILE_PATH"
        echo """
with open('./input.txt', 'r') as file:
    file_data = file.read()
    input_value = '""'


def main(input_value):
    pass

if __name__ == '__main__':
    print(main(input_value))
        """ > "$FILE_PATH"
        echo "Created file: $FILE_PATH"
        FILE_PATH="$DIR_PATH/input.txt"
        echo "" > "$FILE_PATH"
        echo "Created file: $FILE_PATH"
    done
done

echo "All directories and files created successfully."