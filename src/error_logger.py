import logging
import traceback
import sys

def log_custom_error(message, error=None, log_level=logging.ERROR):
    """
    Log a custom error message with optional additional error details.
    
    Args:
        message (str): Custom error message to log
        error (Exception, optional): Optional error object to log additional details
        log_level (int, optional): Logging level, defaults to logging.ERROR
    
    Returns:
        None
    """
    # Configure basic logging if not already configured
    logging.basicConfig(
        level=logging.DEBUG, 
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),  # Log to console
            logging.FileHandler('error.log')    # Log to file
        ]
    )
    
    # Log the custom message
    logging.log(log_level, message)
    
    # If an error is provided, log its details
    if error:
        logging.log(log_level, f"Error Type: {type(error).__name__}")
        logging.log(log_level, f"Error Details: {str(error)}")
        logging.log(log_level, f"Traceback:\n{traceback.format_exc()}")