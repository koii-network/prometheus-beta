import logging
import functools

def log_input_validation(logger=None):
    """
    Decorator to log input validation messages for function arguments.
    
    Args:
        logger (logging.Logger, optional): Custom logger. 
                If not provided, uses the root logger.
    
    Returns:
        Decorator function for logging input validation
    """
    # Use root logger if no logger is provided
    if logger is None:
        logger = logging.getLogger()
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Log input arguments
            logger.info(f"Validating inputs for {func.__name__}")
            
            # Log positional arguments
            for i, arg in enumerate(args):
                logger.debug(f"Positional arg {i}: {arg}")
            
            # Log keyword arguments
            for key, value in kwargs.items():
                logger.debug(f"Keyword arg {key}: {value}")
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

def validate_input(value, validator=None, error_message=None):
    """
    Validate input with optional custom validation.
    
    Args:
        value: Input value to validate
        validator (callable, optional): Custom validation function
        error_message (str, optional): Custom error message
    
    Returns:
        The validated input value
    
    Raises:
        ValueError: If validation fails
    """
    # Use the root logger
    logger = logging.getLogger()
    
    # Log the input validation attempt
    logger.info(f"Validating input: {value}")
    
    # Apply custom validator if provided
    if validator is not None:
        try:
            is_valid = validator(value)
            
            if not is_valid:
                # Use custom error message or generate a default one
                msg = error_message or f"Validation failed for input: {value}"
                logger.error(msg)
                raise ValueError(msg)
            
            logger.info(f"Input {value} passed validation")
        except Exception as e:
            logger.error(f"Validation error: {str(e)}")
            raise
    
    return value