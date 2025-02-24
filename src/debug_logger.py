import logging

def conditional_debug_log(message, debug_enabled=False, logger=None):
    """
    Conditionally log a debug message based on the debug_enabled flag.
    
    Args:
        message (str): The debug message to log
        debug_enabled (bool, optional): Flag to enable/disable debug logging. Defaults to False.
        logger (logging.Logger, optional): Custom logger to use. If None, uses root logger.
    
    Returns:
        bool: True if message was logged, False otherwise
    """
    # If no logger is provided, use the root logger
    if logger is None:
        logger = logging.getLogger()
    
    # Only log if debug is enabled
    if debug_enabled:
        logger.debug(message)
        return True
    
    return False