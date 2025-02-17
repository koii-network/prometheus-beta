import logging
import traceback
import sys

def log_custom_error(message, error=None, log_level=logging.ERROR):
    """
    Log a custom error message with optional additional error details.
    
    :param message: Custom error message to log
    :param error: Optional error object or exception to include additional details
    :param log_level: Logging level (default is logging.ERROR)
    """
    # Configure basic logging if not already configured
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),  # Log to console
            logging.FileHandler('error.log')    # Log to file
        ]
    )
    
    # Log the custom message
    logging.log(log_level, message)
    
    # If an error is provided, log its details
    if error:
        logging.log(log_level, f"Error Details: {str(error)}")
        logging.log(log_level, f"Traceback: {traceback.format_exc()}")
    
    return True  # Indicates successful logging