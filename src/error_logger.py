import logging
import functools
import traceback
import sys

def log_error(message=None):
    """
    A decorator function to log custom error messages when an exception occurs.

    Args:
        message (str, optional): A custom error message to log. 
                                 If None, a default error message will be used.

    Returns:
        callable: A decorator that wraps the original function with error logging.

    Example:
        @log_error("Failed to process data")
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
                # Configure logging to output to stderr
                logging.basicConfig(
                    level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    stream=sys.stderr
                )

                # Use custom message if provided, otherwise create a default
                log_msg = (message or 
                           f"Error in function {func.__name__}: {str(e)}")
                
                # Log the error message
                logging.error(log_msg)
                
                # Log full traceback for debugging
                logging.error(traceback.format_exc())
                
                # Re-raise the exception to maintain original error behavior
                raise
        return wrapper
    return decorator