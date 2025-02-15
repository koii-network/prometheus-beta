import logging
import sys
from typing import Optional

def log_user_input(log_level: str = 'INFO', log_file: Optional[str] = None) -> str:
    """
    Log user input from the command line.
    
    Args:
        log_level (str, optional): Logging level. Defaults to 'INFO'.
        log_file (str, optional): Path to log file. If None, logs to console.
    
    Returns:
        str: The user input that was logged
    
    Raises:
        ValueError: If an invalid log level is provided
    """
    # Configure logging
    numeric_level = getattr(logging, log_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f'Invalid log level: {log_level}')
    
    # Reset any existing loggers
    logging.getLogger().handlers.clear()
    
    # Create logger
    logger = logging.getLogger()
    logger.setLevel(numeric_level)
    
    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
    
    # Create handler
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    else:
        # If no file specified, log to console
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)
    
    # Get user input from command line
    try:
        user_input = input("Enter your message to log: ")
        
        # Log the input
        logger.log(numeric_level, user_input)
        
        return user_input
    except KeyboardInterrupt:
        logger.error("User input was interrupted")
        return ""