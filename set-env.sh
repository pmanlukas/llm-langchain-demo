#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: $0 <service_account_key_file_name>"
    exit 1
fi

KEY_FILE_NAME="$1"
KEY_FILE_PATH="./$KEY_FILE_NAME"  # Use "./" for relative path

echo "File Name: $KEY_FILE_NAME" 
echo "File Path: $KEY_FILE_PATH"

# Check if the file exists
if [ ! -f "$KEY_FILE_PATH" ]; then
    echo "Error: File not found."
    exit 1  # Exit with an error code
fi

# Set the environment variable 
export GOOGLE_APPLICATION_CREDENTIALS="$KEY_FILE_PATH"

# Check if the environment variable is set
if [[ -z "${GOOGLE_APPLICATION_CREDENTIALS}" ]]; then
    echo "Error: GOOGLE_APPLICATION_CREDENTIALS could not be set."
    exit 1  # Exit with an error code
else
    echo "GOOGLE_APPLICATION_CREDENTIALS set to $KEY_FILE_PATH"
fi


