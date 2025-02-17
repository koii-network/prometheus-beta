import json
import os
from datetime import datetime

def log_session_state(session_data, log_dir='logs'):
    """
    Log the state of an interactive session to a JSON file.
    
    Args:
        session_data (dict): A dictionary containing session information.
        log_dir (str, optional): Directory to store log files. Defaults to 'logs'.
    
    Returns:
        str: Path to the created log file
    
    Raises:
        TypeError: If session_data is not a dictionary
        ValueError: If session_data is empty
    """
    # Validate input
    if not isinstance(session_data, dict):
        raise TypeError("Session data must be a dictionary")
    
    if not session_data:
        raise ValueError("Session data cannot be empty")
    
    # Ensure log directory exists
    os.makedirs(log_dir, exist_ok=True)
    
    # Generate unique filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"session_log_{timestamp}.json"
    log_path = os.path.join(log_dir, filename)
    
    # Add timestamp to session data
    session_data['log_timestamp'] = timestamp
    
    # Write session data to JSON file
    with open(log_path, 'w') as log_file:
        json.dump(session_data, log_file, indent=4)
    
    return log_path