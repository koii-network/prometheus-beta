import traceback
import logging
import sys

def log_stack_trace(exception=None, log_level=logging.ERROR, logger=None):
    """
    Log a stack trace with flexible configuration options.
    
    Args:
        exception (Exception, optional): The exception to log. If None, logs the current exception.
        log_level (int, optional): Logging level. Defaults to logging.ERROR.
        logger (logging.Logger, optional): Custom logger. If None, uses root logger.
    
    Returns:
        str: The full stack trace as a string
    """
    # If no logger is provided, use the root logger
    if logger is None:
        logger = logging.getLogger()
    
    # Determine the stack trace to log
    if exception:
        # If an exception is provided, get its traceback
        trace = traceback.format_exception(type(exception), exception, exception.__traceback__)
    else:
        # If no exception is provided, get the current exception's traceback
        exc_type, exc_value, exc_traceback = sys.exc_info()
        
        # If no current exception, return an empty string
        if exc_type is None:
            return ""
        
        trace = traceback.format_exception(exc_type, exc_value, exc_traceback)
    
    # Convert trace to a single string
    trace_str = ''.join(trace)
    
    # Log the stack trace
    logger.log(log_level, f"Stack Trace:\n{trace_str}")
    
    return trace_str