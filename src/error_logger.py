import logging
import traceback
from typing import Any, Callable

def log_error(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    A decorator that logs custom error messages when an exception occurs.
    
    Args:
        func (Callable): The function to be decorated
    
    Returns:
        Callable: A wrapped function with error logging
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # Configure logging if not already configured
            logging.basicConfig(
                level=logging.ERROR, 
                format='%(asctime)s - %(levelname)s - Custom Error: %(message)s'
            )
            
            # Log the full error details
            error_message = f"Error in {func.__name__}: {str(e)}"
            logging.error(error_message)
            
            # Log the full traceback for debugging
            logging.error(traceback.format_exc())
            
            # Re-raise the exception to maintain original error handling
            raise
    
    return wrapper