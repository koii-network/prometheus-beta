import traceback
import logging
import sys

def log_stack_trace(exception=None, log_level=logging.ERROR):
    """
    Log a stack trace with optional exception handling.
    
    Args:
        exception (Exception, optional): The exception to log. Defaults to None.
        log_level (int, optional): Logging level. Defaults to logging.ERROR.
    
    Returns:
        str: The formatted stack trace string
    """
    # Configure logging if not already configured
    logging.basicConfig(
        level=logging.DEBUG, 
        format='%(asctime)s - %(levelname)s: %(message)s'
    )
    
    # If no exception provided, get the current exception
    if exception is None:
        exc_info = sys.exc_info()
        if exc_info[0] is None:
            return "No exception found to log."
        exception = exc_info[1]
    
    # Get the full stack trace as a string
    stack_trace = traceback.format_exc()
    
    # Log the stack trace
    logging.log(log_level, f"Exception: {type(exception).__name__} - {str(exception)}")
    logging.log(log_level, f"Stack Trace:\n{stack_trace}")
    
    return stack_trace