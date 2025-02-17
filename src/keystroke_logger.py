import logging
import datetime
import os

def log_keystrokes(key):
    """
    Log keystrokes to a log file with timestamp.
    
    Args:
        key (str): The key that was pressed
    
    Raises:
        ValueError: If the input is not a valid key
        IOError: If there's an issue writing to the log file
    """
    # Validate input
    if not isinstance(key, str) or len(key) != 1:
        raise ValueError("Input must be a single character")
    
    # Ensure logs directory exists
    log_dir = 'logs'
    os.makedirs(log_dir, exist_ok=True)
    
    # Create a log file with today's date
    log_file = os.path.join(log_dir, f'keystrokes_{datetime.date.today().isoformat()}.log')
    
    # Configure logging
    logging.basicConfig(
        filename=log_file, 
        level=logging.INFO, 
        format='%(asctime)s - Keystroke: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Log the keystroke
    logging.info(key)
    
    return True