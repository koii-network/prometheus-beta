import logging
import functools
import traceback
from typing import Callable, Any

def log_error(message: str = "An error occurred"):
    """
    A decorator function to log custom error messages when an exception occurs.

    Args:
        message (str, optional): Custom error message to log. Defaults to "An error occurred".

    Returns:
        Callable: A decorator that logs errors and re-raises them.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                return func(*args, **kwargs)
            except Exception as e:
                # Configure logging to output to console and potentially a file
                logging.basicConfig(
                    level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s'
                )
                
                # Log the custom message along with the full traceback
                logging.error(f"{message}: {str(e)}")
                logging.error(traceback.format_exc())
                
                # Re-raise the exception to allow further error handling if needed
                raise
        return wrapper
    return decorator