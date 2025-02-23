import datetime
import os
import json

def log_data_with_timestamp(data, log_file='logs/data_log.json'):
    """
    Log data with a timestamp to a JSON file.

    Args:
        data (dict): The data to be logged
        log_file (str, optional): Path to the log file. Defaults to 'logs/data_log.json'

    Raises:
        TypeError: If data is not a dictionary
        ValueError: If data is empty
    """
    # Validate input
    if not isinstance(data, dict):
        raise TypeError("Input must be a dictionary")
    
    if not data:
        raise ValueError("Data cannot be empty")

    # Ensure log directory exists
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    # Add timestamp to the data
    log_entry = {
        'timestamp': datetime.datetime.now().isoformat(),
        'data': data
    }

    # Append to log file
    try:
        # If file exists, read and append
        if os.path.exists(log_file):
            with open(log_file, 'r+') as f:
                try:
                    logs = json.load(f)
                except json.JSONDecodeError:
                    logs = []
                
                logs.append(log_entry)
                f.seek(0)
                json.dump(logs, f, indent=2)
                f.truncate()
        else:
            # Create new log file
            with open(log_file, 'w') as f:
                json.dump([log_entry], f, indent=2)
    
    except IOError as e:
        raise IOError(f"Error writing to log file: {e}")

    return log_entry