import traceback
import logging
import sys
from typing import Optional, Union, Callable, Any

def log_stack_trace(
    exception: Optional[Union[Exception, BaseException]] = None, 
    logger: Optional[logging.Logger] = None, 
    log_level: int = logging.ERROR
) -> str:
    """
    Log a stack trace for an exception or the current exception.
    
    Args:
        exception (Optional[Exception]): The exception to log. 
            If None, uses the current exception from sys.exc_info().
        logger (Optional[logging.Logger]): Logger to use. 
            If None, uses the root logger.
        log_level (int): Logging level to use. Defaults to logging.ERROR.
    
    Returns:
        str: The formatted stack trace as a string.
    """
    # Use the provided logger or get the root logger
    log = logger or logging.getLogger()
    
    try:
        # If no exception is provided, get the current exception
        if exception is None:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            
            # If no current exception, return empty string
            if exc_type is None:
                return ""
        else:
            # Use the provided exception
            exc_type = type(exception)
            exc_value = exception
            exc_traceback = exception.__traceback__
        
        # Format the stack trace as a string
        stack_trace = ''.join(traceback.format_exception(
            exc_type, 
            exc_value, 
            exc_traceback
        ))
        
        # Log the stack trace
        log.log(log_level, stack_trace)
        
        return stack_trace
    
    except Exception as e:
        # Fallback logging in case of any issues with stack trace logging
        log.error(f"Error while logging stack trace: {e}")
        return ""