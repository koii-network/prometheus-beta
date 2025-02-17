import logging
import functools

def log_input_validation(logger=None):
    """
    Decorator to log input validation messages.
    
    Args:
        logger (logging.Logger, optional): Custom logger. 
                If not provided, uses the root logger.
    
    Returns:
        Decorated function that logs input validation details.
    """
    if logger is None:
        logger = logging.getLogger(__name__)
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Log input arguments
            logger.info(f"Validating inputs for {func.__name__}")
            logger.debug(f"Positional args: {args}")
            logger.debug(f"Keyword args: {kwargs}")
            
            try:
                # Perform validation
                result = func(*args, **kwargs)
                logger.info(f"Input validation successful for {func.__name__}")
                return result
            except ValueError as ve:
                logger.error(f"Input validation failed for {func.__name__}: {ve}")
                raise
            except TypeError as te:
                logger.error(f"Input type validation failed for {func.__name__}: {te}")
                raise
        
        return wrapper
    
    return decorator