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
    Log a stack trace with optional flexibility in logging mechanism.

    Args:
        exception (Optional[Exception]): The exception to log. If None, logs current exception.
        logger (Optional[logging.Logger]): Custom logger. If None, uses root logger.
        log_level (int): Logging level (default is logging.ERROR)

    Returns:
        str: The formatted stack trace as a string

    Raises:
        TypeError: If an invalid logger or log level is provided
    """
    # Validate inputs
    if logger is not None and not isinstance(logger, logging.Logger):
        raise TypeError("Logger must be a logging.Logger instance")

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
                return "No active exception found."
            
            stack_trace = ''.join(traceback.format_exception(
                exc_type, exc_value, exc_traceback
            ))

        # Use provided logger or root logger
        log_func = (logger or logging).log

        # Log the stack trace
        log_func(log_level, f"Stack Trace:\n{stack_trace}")

        return stack_trace

    except Exception as e:
        # Fallback logging in case of any issues with primary logging
        print(f"Error logging stack trace: {e}")
        return ""