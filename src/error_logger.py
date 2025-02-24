import logging
import functools
import traceback
import sys
import os

def log_error(message=None):
    """
    A decorator function to log custom error messages when an exception occurs.

    Args:
        message (str, optional): Custom error message to log. 
                                 If None, uses the default exception message.

    Returns:
        callable: A decorator that wraps the original function with error logging.

    Example:
        @log_error("Something went wrong in the calculation")
        def some_function():
            # Function implementation
            pass
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                # Create logs directory if it doesn't exist
                os.makedirs('logs', exist_ok=True)
                
                # Configure logging to output to both console and file
                logger = logging.getLogger(func.__name__)
                logger.setLevel(logging.ERROR)
                
                # Create file handler
                file_handler = logging.FileHandler('logs/error.log')
                file_handler.setLevel(logging.ERROR)
                
                # Create console handler
                console_handler = logging.StreamHandler(sys.stderr)
                console_handler.setLevel(logging.ERROR)
                
                # Create formatter
                formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
                file_handler.setFormatter(formatter)
                console_handler.setFormatter(formatter)
                
                # Add handlers to logger if not already added
                if not logger.handlers:
                    logger.addHandler(file_handler)
                    logger.addHandler(console_handler)
                
                # Determine the error message
                error_msg = message or str(e)
                
                # Log the error with full traceback
                logger.error(f"{error_msg}\nException Details:\n{traceback.format_exc()}")
                
                # Re-raise the exception to allow further error handling if needed
                raise
        return wrapper
    return decorator