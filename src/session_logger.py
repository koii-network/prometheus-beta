import json
import os
import datetime
import traceback

def log_session_state(session_data, log_dir='logs'):
    """
    Log the state of an interactive session to a JSON file.
    
    Args:
        session_data (dict): A dictionary containing session information
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
    
    # Generate a unique filename with timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = f"session_log_{timestamp}.json"
    log_path = os.path.join(log_dir, log_filename)
    
    # Add timestamp to session data
    session_data['timestamp'] = timestamp
    
    # Write session data to JSON file
    try:
        with open(log_path, 'w') as log_file:
            json.dump(session_data, log_file, indent=4)
        return log_path
    except Exception as e:
        raise IOError(f"Could not write log file: {e}")