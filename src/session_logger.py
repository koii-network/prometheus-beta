import json
import os
from datetime import datetime

def log_session_state(session_data, log_dir='logs'):
    """
    Log the state of an interactive session to a JSON file.
    
    Args:
        session_data (dict): A dictionary containing session state information
        log_dir (str, optional): Directory to save log files. Defaults to 'logs'.
    
    Returns:
        str: Path to the created log file
    
    Raises:
        ValueError: If session_data is not a dictionary
        IOError: If there are issues creating the log directory or writing the file
    """
    # Validate input
    if not isinstance(session_data, dict):
        raise ValueError("Session data must be a dictionary")
    
    # Create logs directory if it doesn't exist
    os.makedirs(log_dir, exist_ok=True)
    
    # Generate unique filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"session_state_{timestamp}.json"
    log_path = os.path.join(log_dir, filename)
    
    # Add timestamp to session data
    session_data['logged_at'] = timestamp
    
    # Write session data to JSON file
    try:
        with open(log_path, 'w') as log_file:
            json.dump(session_data, log_file, indent=4)
        return log_path
    except IOError as e:
        raise IOError(f"Could not write log file: {e}")