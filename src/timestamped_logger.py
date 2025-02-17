import logging
from datetime import datetime
import os

def log_with_timestamp(message, log_level='INFO', log_file='app.log'):
    """
    Log a message with a timestamp to both console and file.
    
    Args:
        message (str): The message to log
        log_level (str, optional): Logging level. Defaults to 'INFO'.
        log_file (str, optional): Path to the log file. Defaults to 'app.log'.
    
    Raises:
        ValueError: If an invalid log level is provided
    """
    # Ensure logs directory exists
    os.makedirs('logs', exist_ok=True)
    
    # Configure logging
    log_path = os.path.join('logs', log_file)
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename=log_path,
        filemode='a'
    )
    
    # Validate log level
    valid_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    if log_level.upper() not in valid_levels:
        raise ValueError(f"Invalid log level. Must be one of {valid_levels}")
    
    # Log the message
    logger = logging.getLogger()
    log_method = getattr(logger, log_level.lower())
    log_method(message)
    
    # Also print to console
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {log_level.upper()} - {message}")
    
    return True