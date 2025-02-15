import json
import os
import datetime

def log_session_state(session_data, log_dir='logs'):
    """
    Log the state of an interactive session to a JSON file.
    
    Args:
        session_data (dict): A dictionary containing session information.
        log_dir (str, optional): Directory to store log files. Defaults to 'logs'.
    
    Returns:
        str: Path to the created log file.
    
    Raises:
        TypeError: If session_data is not a dictionary.
        ValueError: If session_data is empty.
    """
    # Validate input
    if not isinstance(session_data, dict):
        raise TypeError("session_data must be a dictionary")
    
    if not session_data:
        raise ValueError("session_data cannot be empty")
    
    # Create logs directory if it doesn't exist
    os.makedirs(log_dir, exist_ok=True)
    
    # Generate unique filename with timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = f"session_log_{timestamp}.json"
    log_path = os.path.join(log_dir, log_filename)
    
    # Add timestamp to session data
    session_data['log_timestamp'] = timestamp
    
    # Write session data to JSON file
    with open(log_path, 'w') as log_file:
        json.dump(session_data, log_file, indent=2)
    
    return log_path