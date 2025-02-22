import logging
import functools

def log_input_validation(logger=None):
    """
    Decorator to log input validation messages.
    
    Args:
        logger (logging.Logger, optional): Logger to use. 
               If not provided, uses the root logger.
    
    Returns:
        Decorator function for logging input validation
    """
    if logger is None:
        logger = logging.getLogger()
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Log input arguments
            logger.info(f"Validating inputs for {func.__name__}")
            logger.debug(f"Positional args: {args}")
            logger.debug(f"Keyword args: {kwargs}")
            
            try:
                # Call the original function
                result = func(*args, **kwargs)
                logger.info(f"Input validation successful for {func.__name__}")
                return result
            except ValueError as ve:
                # Log validation errors
                logger.error(f"Input validation failed for {func.__name__}: {str(ve)}")
                raise
            except TypeError as te:
                # Log type-related validation errors
                logger.error(f"Input type validation failed for {func.__name__}: {str(te)}")
                raise
        
        return wrapper
    return decorator