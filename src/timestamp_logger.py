import datetime
import os

def log_with_timestamp(data, log_file='app.log'):
    """
    Log data with a timestamp to a specified log file.
    
    Args:
        data (str): The data to be logged
        log_file (str, optional): Path to the log file. Defaults to 'app.log'
    
    Returns:
        str: The full log entry that was written
    """
    # Ensure the directory exists
    os.makedirs(os.path.dirname(log_file) or '.', exist_ok=True)
    
    # Create timestamp
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Create log entry
    log_entry = f"[{timestamp}] {data}\n"
    
    # Write to log file
    with open(log_file, 'a') as f:
        f.write(log_entry)
    
    return log_entry