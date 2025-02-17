import datetime
import json
import os

def log_with_timestamp(data, log_file='logs/app.log'):
    """
    Log data with a timestamp to a specified log file.
    
    Args:
        data (dict or str): The data to be logged
        log_file (str, optional): Path to the log file. Defaults to 'logs/app.log'
    
    Raises:
        TypeError: If data is not a dictionary or string
        IOError: If there are issues creating the log directory or writing to the file
    """
    # Ensure the logs directory exists
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    # Get current timestamp
    timestamp = datetime.datetime.now().isoformat()
    
    # Prepare log entry
    if isinstance(data, dict):
        log_entry = {
            'timestamp': timestamp,
            'data': data
        }
        log_text = json.dumps(log_entry) + '\n'
    elif isinstance(data, str):
        log_entry = {
            'timestamp': timestamp,
            'message': data
        }
        log_text = json.dumps(log_entry) + '\n'
    else:
        raise TypeError("Data must be a dictionary or string")
    
    # Write to log file
    try:
        with open(log_file, 'a') as f:
            f.write(log_text)
    except IOError as e:
        raise IOError(f"Could not write to log file: {e}")
    
    return log_entry