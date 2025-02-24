import logging
import functools
import traceback
import sys

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
                # Configure logging to output to both console and file
                logging.basicConfig(
                    level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s: %(message)s',
                    handlers=[
                        logging.FileHandler('error.log'),
                        logging.StreamHandler(sys.stderr)
                    ]
                )

                # Determine the error message
                error_msg = message or str(e)
                
                # Log the error with full traceback
                logging.error(f"{error_msg}\nException Details:\n{traceback.format_exc()}")
                
                # Re-raise the exception to allow further error handling if needed
                raise
        return wrapper
    return decorator