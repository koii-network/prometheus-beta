import datetime
import os

def log_with_timestamp(data, log_file='app.log'):
    """
    Log data with a timestamp to a specified log file.
    
    Args:
        data (str): The message or data to be logged
        log_file (str, optional): Path to the log file. Defaults to 'app.log'
    
    Raises:
        TypeError: If data is not a string
        IOError: If there are issues writing to the log file
    """
    # Validate input
    if not isinstance(data, str):
        raise TypeError("Log data must be a string")
    
    # Ensure the log directory exists
    os.makedirs(os.path.dirname(log_file) or '.', exist_ok=True)
    
    # Get current timestamp
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Create log entry
    log_entry = f"[{timestamp}] {data}\n"
    
    # Write to log file
    try:
        with open(log_file, 'a') as f:
            f.write(log_entry)
    except IOError as e:
        raise IOError(f"Error writing to log file: {e}")
    
    return log_entry.strip()