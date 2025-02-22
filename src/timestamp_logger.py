import datetime
import os
import json
from typing import Any, Union

def log_with_timestamp(data: Any, log_file: str = 'logs/app_log.json', 
                       log_level: str = 'INFO') -> None:
    """
    Log data with a timestamp to a JSON log file.
    
    Args:
        data (Any): The data to be logged (will be converted to JSON)
        log_file (str, optional): Path to the log file. Defaults to 'logs/app_log.json'
        log_level (str, optional): Logging level. Defaults to 'INFO'
    
    Raises:
        ValueError: If log_level is not a valid level
        IOError: If there are issues writing to the log file
    """
    # Validate log level
    valid_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    if log_level not in valid_levels:
        raise ValueError(f"Invalid log level. Must be one of {valid_levels}")
    
    # Create logs directory if it doesn't exist
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    # Prepare log entry
    log_entry = {
        'timestamp': datetime.datetime.now().isoformat(),
        'level': log_level,
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
        else:
            # Create new log file
            with open(log_file, 'w') as f:
                json.dump([log_entry], f, indent=2)
    except IOError as e:
        raise IOError(f"Error writing to log file: {e}")