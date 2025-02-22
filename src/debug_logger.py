import logging
import os

def conditional_debug_log(message, debug_mode=None):
    """
    Conditionally log a debug message based on environment or explicit debug mode.
    
    Args:
        message (str): The debug message to log
        debug_mode (bool, optional): Explicit debug mode override. 
            If None, checks the DEBUG environment variable.
    
    Returns:
        bool: True if message was logged, False otherwise
    """
    # Determine debug mode: 
    # 1. Use explicit debug_mode if provided
    # 2. Check DEBUG environment variable 
    # 3. Default to False if not set
    if debug_mode is None:
        debug_mode = os.environ.get('DEBUG', '').lower() in ['1', 'true', 'yes']
    
    # Configure logging if not already configured
    logging.basicConfig(
        level=logging.DEBUG, 
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    # Log only if debug mode is True
    if debug_mode:
        logging.debug(message)
        return True
    
    return False