import logging
import traceback
import sys

def log_custom_error(error_message, exception=None, log_level=logging.ERROR):
    """
    Log a custom error message with optional exception details.
    
    Args:
        error_message (str): Custom error message to log
        exception (Exception, optional): Exception object to log additional details
        log_level (int, optional): Logging level (default is logging.ERROR)
    
    Returns:
        None
    """
    # Configure logging if not already configured
    logging.basicConfig(
        level=logging.DEBUG, 
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    
    # Log the custom error message
    logging.log(log_level, error_message)
    
    # If an exception is provided, log its details
    if exception:
        logging.log(log_level, f"Exception Type: {type(exception).__name__}")
        logging.log(log_level, f"Exception Details: {str(exception)}")
        
        # Log the full traceback
        logging.log(log_level, "Traceback:\n" + 
                    ''.join(traceback.format_tb(sys.exc_info()[2])))