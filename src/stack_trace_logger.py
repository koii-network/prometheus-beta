import traceback
import logging
import sys

def log_stack_trace(exception=None, log_level=logging.ERROR, logger=None):
    """
    Log a stack trace with optional customization.
    
    :param exception: Optional exception object to log. If None, logs the current exception.
    :param log_level: Logging level (default is logging.ERROR)
    :param logger: Optional logger instance. If None, uses root logger.
    :return: Formatted stack trace string
    """
    # Use the provided logger or get the root logger
    log = logger or logging.getLogger()
    
    # Determine the stack trace
    if exception:
        # If an exception is provided, format its stack trace
        stack_trace = ''.join(traceback.format_exception(type(exception), exception, exception.__traceback__))
    else:
        # If no exception is provided, get the current exception's stack trace
        exc_type, exc_value, exc_traceback = sys.exc_info()
        
        # Check if there's an active exception
        if exc_type is None:
            return "No active exception found."
        
        stack_trace = ''.join(traceback.format_exception(exc_type, exc_value, exc_traceback))
    
    # Log the stack trace
    log.log(log_level, f"Stack Trace:\n{stack_trace}")
    
    return stack_trace