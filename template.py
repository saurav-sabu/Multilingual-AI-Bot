# Importing the modules
import os
import logging
from pathlib import Path

# Configure the logging module to display log messages with timestamp and message format
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: [%(message)s]')

# List of files and directories that need to be created in the project structure
list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "requirements.txt",
    "setup.py",
    "app.py",
    "experiment/trial.ipynb",
    ".env"
]


# Iterate over each file path in the list
for file_path in list_of_files:

    # Convert the file path to a Path object for better handling of filesystem paths
    file_path = Path(file_path)

    # Split the file path into directory and filename
    file_dir, file_name = os.path.split(file_path)

    # If there is a directory path (i.e., it's not the root), create the directory if it doesn't exist
    if file_dir != "":
        logging.info(f"Created directory {file_dir}")
        os.makedirs(file_dir,exist_ok=True) # Create directories recursively if needed

    # If the file does not exist or is empty, create the file
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) == 0):
        with open(file_path,"w") as f:
            logging.info(f"{file_path} created")
            pass

    
