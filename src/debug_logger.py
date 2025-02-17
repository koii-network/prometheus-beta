import logging
import os

def conditional_debug_log(message, debug_enabled=None):
    """
    Conditionally log a debug message based on environment or explicit flag.
    
    Args:
        message (str): The debug message to log
        debug_enabled (bool, optional): Explicit debug flag. 
            If None, checks the DEBUG environment variable.
    
    Returns:
        bool: Whether the message was logged
    """
    # Determine if debug is enabled
    if debug_enabled is None:
        debug_enabled = os.environ.get('DEBUG', 'false').lower() in ['true', '1', 'yes']
    
    # Configure logging if not already configured
    if not logging.getLogger().handlers:
        logging.basicConfig(level=logging.DEBUG if debug_enabled else logging.INFO, 
                            format='%(asctime)s - %(levelname)s - %(message)s')
    
    # Log debug message if enabled
    if debug_enabled:
        logging.debug(message)
        return True
    
    return False