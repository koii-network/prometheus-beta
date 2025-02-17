import logging

def log_warning(message):
    """
    Log a warning message to the console.
    
    Args:
        message (str): The warning message to log.
    """
    # Configure logging to display warning messages to console
    logging.basicConfig(level=logging.WARNING, 
                        format='%(levelname)s: %(message)s')
    
    # Log the warning message
    logging.warning(message)