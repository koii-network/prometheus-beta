import logging
import functools

def conditional_debug_log(condition=True, logger=None):
    """
    A decorator that conditionally logs debug messages based on a given condition.

    Args:
        condition (bool, optional): Whether debug logging should be enabled. 
                                    Defaults to True.
        logger (logging.Logger, optional): Logger to use. 
                                           Defaults to root logger if not provided.

    Returns:
        callable: A decorator function that conditionally logs debug messages.

    Example:
        >>> @conditional_debug_log(condition=DEBUG_MODE)
        ... def my_function():
        ...     # This will only log if DEBUG_MODE is True
        ...     log.debug("Debug message will only appear if condition is met")
    """
    # Use root logger if no logger is provided
    if logger is None:
        logger = logging.getLogger()

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Only log debug message if condition is True
            if condition:
                logger.debug(f"Entering function: {func.__name__}")
                logger.debug(f"Arguments: args={args}, kwargs={kwargs}")
            
            # Execute the original function
            result = func(*args, **kwargs)
            
            # Only log debug message if condition is True
            if condition:
                logger.debug(f"Exiting function: {func.__name__}")
                logger.debug(f"Return value: {result}")
            
            return result
        return wrapper
    return decorator