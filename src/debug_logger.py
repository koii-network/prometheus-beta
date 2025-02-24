import logging
import functools

def conditional_debug_log(condition=True, logger=None):
    """
    Decorator to conditionally log debug messages.

    Args:
        condition (bool, optional): Whether debugging is enabled. Defaults to True.
        logger (logging.Logger, optional): Logger to use. Defaults to root logger.

    Returns:
        Callable: Decorated function that conditionally logs debug messages.

    Example:
        >>> @conditional_debug_log(condition=True)
        ... def example_function(x):
        ...     return x * 2
        >>> example_function(5)  # Will log debug message
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Use provided logger or get the root logger
            log = logger or logging.getLogger()
            
            # Log debug message if condition is True
            if condition:
                log.debug(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
            
            # Execute the original function
            result = func(*args, **kwargs)
            
            # Log debug message about return value if condition is True
            if condition:
                log.debug(f"{func.__name__} returned: {result}")
            
            return result
        return wrapper
    return decorator