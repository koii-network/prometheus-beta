import logging
import os

def conditional_debug_log(message, condition=None, logger=None):
    """
    Conditionally log a debug message based on an optional condition.
    
    Args:
        message (str): The debug message to log
        condition (bool, optional): A condition that must be True to log the message. 
                                    If None, uses environment variable DEBUG.
        logger (logging.Logger, optional): Custom logger. If None, uses root logger.
    
    Returns:
        bool: True if message was logged, False otherwise
    """
    # Use root logger if no logger is provided
    if logger is None:
        logger = logging.getLogger()
    
    # Determine logging condition
    if condition is None:
        # Check environment variable, default to False if not set
        condition = os.environ.get('DEBUG', '').lower() in ['1', 'true', 'yes']
    
    # Log the message if condition is True
    if condition:
        logger.debug(message)
        return True
    
    return False