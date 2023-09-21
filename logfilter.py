import os
import time

# Specify the ConfigMap file path
config_map = '/config/LOG_LEVEL'

# Specify the directory path
folder_path = '/var/log/app'

# List all files in the directory
files = os.listdir(folder_path)

# Check if there is exactly one file in the directory
if len(files) == 1:
    # Construct the full path to the file
    log_file_path = os.path.join(folder_path, files[0])
else:
    print(f"Expected one file in the directory, but found {len(files)} files.")
    exit(1)

def getLogLevel():
    # Get the desired log level from the LOG_LEVEL variable in the ConfigMap mounted as a file inside volume.   
    
    # Specify default log level
    log_level = 0
    allowed_log_levels = ["ERROR"]

    try:
        with open(config_map, "r") as G: 
            log_level=int(G.read()) 

    except FileNotFoundError:
        print(f"Configmap file not found: {config_map}")
        exit(1)

    # Define the allowed log levels based on the log_level setting    
    if log_level in [1, 2]:        
        if log_level >= 1:
            allowed_log_levels.append("WARNING")
        if log_level >= 2:
            allowed_log_levels.append("INFO")
        
    return allowed_log_levels

def tail(filename):
    try:
        with open(filename, 'r') as file:
            file.seek(0, os.SEEK_END)
            while True:
                line = file.readline()
                if not line:
                    time.sleep(0.1)
                    continue
                yield line
    except FileNotFoundError:
        print(f"Log file not found: {filename}")
        exit(1)

# Main
for line in tail(log_file_path):
    for log_level in getLogLevel():
        if log_level in line:
            print(line.strip())
            break
