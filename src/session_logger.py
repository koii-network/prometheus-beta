import os
import json
from datetime import datetime
import traceback

def log_session_state(session_data, log_dir='logs'):
    """
    Log the state of an interactive session to a JSON file.
    
    Args:
        session_data (dict): A dictionary containing session state information
        log_dir (str, optional): Directory to store log files. Defaults to 'logs'.
    
    Returns:
        str: Path to the created log file
    
    Raises:
        ValueError: If session_data is not a dictionary
        IOError: If there are issues creating the log directory or writing the file
    """
    # Validate input
    if not isinstance(session_data, dict):
        raise ValueError("Session data must be a dictionary")
    
    # Ensure log directory exists
    try:
        os.makedirs(log_dir, exist_ok=True)
    except Exception as e:
        raise IOError(f"Could not create log directory: {e}")
    
    # Generate unique filename with timestamp and microseconds
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    log_filename = f"session_log_{timestamp}.json"
    log_path = os.path.join(log_dir, log_filename)
    
    # Add metadata to session data
    full_log_data = {
        "timestamp": timestamp,
        "session_details": session_data,
        "environment": {
            "python_version": os.sys.version,
            "platform": os.sys.platform
        }
    }
    
    # Write log file
    try:
        with open(log_path, 'w') as log_file:
            json.dump(full_log_data, log_file, indent=4)
    except Exception as e:
        raise IOError(f"Could not write log file: {e}")
    
    return log_path