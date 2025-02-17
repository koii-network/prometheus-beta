import logging
import functools

def log_input_validation(logger=None):
    """
    Decorator to log input validation messages.
    
    Args:
        logger (logging.Logger, optional): Logger to use. 
                If not provided, creates a default logger.
    
    Returns:
        Decorator function for input validation logging
    """
    # Use a default logger if none is provided
    if logger is None:
        logger = logging.getLogger(__name__)
        # Set up basic logging configuration if no handler exists
        if not logger.handlers:
            logging.basicConfig(level=logging.INFO, 
                                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Log input validation information
            logger.info(f"Validating inputs for function: {func.__name__}")
            
            # Log positional arguments
            if args:
                logger.debug(f"Positional arguments: {args}")
            
            # Log keyword arguments
            if kwargs:
                logger.debug(f"Keyword arguments: {kwargs}")
            
            # Perform the original function call
            try:
                result = func(*args, **kwargs)
                logger.info(f"Input validation successful for {func.__name__}")
                return result
            except ValueError as ve:
                # Log validation errors
                logger.error(f"Input validation error in {func.__name__}: {str(ve)}")
                raise
            except TypeError as te:
                # Log type-related validation errors
                logger.error(f"Input type validation error in {func.__name__}: {str(te)}")
                raise
        
        return wrapper
    
    return decorator