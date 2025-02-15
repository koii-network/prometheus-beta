import traceback
import logging
import sys

def log_stack_trace(exception=None, log_level=logging.ERROR, logger=None):
    """
    Log the stack trace of an exception or the current stack trace.
    
    Args:
        exception (Exception, optional): The exception to log. If None, logs current stack trace.
        log_level (int, optional): Logging level. Defaults to logging.ERROR.
        logger (logging.Logger, optional): Logger to use. If None, uses root logger.
    
    Returns:
        str: The formatted stack trace string
    """
    # If no logger is provided, use the root logger
    if logger is None:
        logger = logging.getLogger()
    
    # Determine the stack trace
    if exception:
        # If an exception is provided, get its traceback
        stack_trace = ''.join(traceback.format_exception(type(exception), exception, exception.__traceback__))
    else:
        # If no exception, get the current stack trace
        stack_trace = ''.join(traceback.format_stack())
    
    # Log the stack trace
    logger.log(log_level, f"Stack Trace:\n{stack_trace}")
    
    return stack_trace