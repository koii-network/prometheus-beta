import datetime
import os

def log_with_timestamp(message, log_file='app.log'):
    """
    Log a message with a timestamp to a specified log file.
    
    Args:
        message (str): The message to log
        log_file (str, optional): Path to the log file. Defaults to 'app.log'
    
    Returns:
        str: The full log message that was written
    """
    # Ensure the directory exists
    os.makedirs(os.path.dirname(log_file) or '.', exist_ok=True)
    
    # Create timestamp
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Create log message
    log_entry = f'[{timestamp}] {message}\n'
    
    # Write to log file
    with open(log_file, 'a') as f:
        f.write(log_entry)
    
    return log_entry.strip()