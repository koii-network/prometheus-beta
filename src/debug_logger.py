import logging
import functools

def conditional_debug_log(condition=True, logger=None):
    """
    A decorator for conditionally logging debug messages.
    
    Args:
        condition (bool, optional): Whether debug logging is enabled. Defaults to True.
        logger (logging.Logger, optional): Logger to use. If None, uses root logger.
    
    Returns:
        Decorator function that conditionally logs debug messages.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Use provided logger or get root logger
            log = logger or logging.getLogger()
            
            # Log function entry if condition is True
            if condition:
                log.debug(f"Entering function: {func.__name__}")
                log.debug(f"Args: {args}")
                log.debug(f"Kwargs: {kwargs}")
            
            # Execute the function
            result = func(*args, **kwargs)
            
            # Log function exit and return value if condition is True
            if condition:
                log.debug(f"Exiting function: {func.__name__}")
                log.debug(f"Return value: {result}")
            
            return result
        return wrapper
    return decorator