import datetime
import os

def log_with_timestamp(data, log_file='logs/app.log'):
    """
    Log data with a timestamp to a specified log file.
    
    Args:
        data (str): The data to be logged
        log_file (str, optional): Path to the log file. Defaults to 'logs/app.log'
    
    Raises:
        TypeError: If data is not a string
        IOError: If there are issues creating the log directory or writing to the file
    """
    # Ensure the log directory exists
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    # Validate input
    if not isinstance(data, str):
        raise TypeError("Log data must be a string")
    
    # Get current timestamp
    timestamp = datetime.datetime.now().isoformat()
    
    # Create log entry
    log_entry = f"{timestamp} - {data}\n"
    
    # Write to log file
    try:
        with open(log_file, 'a') as f:
            f.write(log_entry)
    except IOError as e:
        raise IOError(f"Error writing to log file: {e}")
    
    return log_entry.strip()