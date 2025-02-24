import traceback
import logging
import sys
from typing import Optional, Union, Callable, Any

def log_stack_trace(
    exception: Optional[Union[Exception, BaseException]] = None, 
    logger: Optional[Union[logging.Logger, Any]] = None, 
    log_level: int = logging.ERROR
) -> str:
    """
    Log a stack trace with optional flexibility in logging mechanism.

    Args:
        exception (Optional[Exception]): The exception to log. If None, logs current exception.
        logger (Optional[Logger]): Custom logger. If None, uses root logger.
        log_level (int): Logging level (default is logging.ERROR)

    Returns:
        str: The formatted stack trace as a string

    Raises:
        TypeError: If an invalid log level is provided
    """
    # Determine logging function
    def default_log_func(level, message):
        print(message)

    # Select appropriate logging function
    if logger is None:
        log_func = default_log_func
    elif hasattr(logger, 'log'):
        log_func = logger.log
    elif callable(logger):
        log_func = logger
    else:
        log_func = default_log_func

    try:
        # Determine the stack trace
        if exception is not None:
            # If a specific exception is provided, get its traceback
            stack_trace = ''.join(traceback.format_exception(
                type(exception), exception, exception.__traceback__
            ))
        else:
            # If no exception provided, get the current exception
            exc_type, exc_value, exc_traceback = sys.exc_info()
            if exc_type is None:
                stack_trace = "No active exception found."
                log_func(log_level, stack_trace)
                return stack_trace
            
            stack_trace = ''.join(traceback.format_exception(
                exc_type, exc_value, exc_traceback
            ))

        # Log the stack trace
        log_func(log_level, f"Stack Trace:\n{stack_trace}")

        return stack_trace

    except Exception as e:
        # Fallback logging in case of any issues with primary logging
        print(f"Error logging stack trace: {e}")
        return ""