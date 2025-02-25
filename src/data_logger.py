import datetime
import json
import os

def log_data(data, log_file='logs/data_log.json'):
    """
    Log data with a timestamp to a JSON log file.
    
    Args:
        data (dict): The data to be logged
        log_file (str, optional): Path to the log file. Defaults to 'logs/data_log.json'
    
    Returns:
        bool: True if logging was successful, False otherwise
    """
    # Ensure the logs directory exists
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    # Create log entry with timestamp
    log_entry = {
        'timestamp': datetime.datetime.now().isoformat(),
        'data': data
    }
    
    try:
        # If file exists, append to it; otherwise, create a new list
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
            with open(log_file, 'w') as f:
                json.dump([log_entry], f, indent=2)
        
        return True
    except (IOError, TypeError) as e:
        print(f"Error logging data: {e}")
        return False