import logging
import functools
import inspect

def log_input_validation(logger=None, validate_types=True):
    """
    Decorator to log input validation messages.
    
    Args:
        logger (logging.Logger, optional): Custom logger. 
                If not provided, uses the root logger.
        validate_types (bool, optional): Whether to validate input types.
                Defaults to True.
    
    Returns:
        Decorator function for input validation logging.
    """
    if logger is None:
        logger = logging.getLogger()
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Log input arguments
            logger.info(f"Validating inputs for function: {func.__name__}")
            logger.debug(f"Positional arguments: {args}")
            logger.debug(f"Keyword arguments: {kwargs}")
            
            # Perform type validation if enabled
            if validate_types:
                sig = inspect.signature(func)
                bound_arguments = sig.bind(*args, **kwargs)
                bound_arguments.apply_defaults()
                
                for param_name, param in sig.parameters.items():
                    arg_value = bound_arguments.arguments[param_name]
                    
                    if param.annotation != inspect.Parameter.empty:
                        if not isinstance(arg_value, param.annotation):
                            error_msg = (f"Invalid type for parameter '{param_name}'. "
                                         f"Expected {param.annotation}, "
                                         f"got {type(arg_value)}")
                            logger.error(error_msg)
                            raise TypeError(error_msg)
            
            try:
                # Call the original function
                result = func(*args, **kwargs)
                logger.info(f"Input validation successful for {func.__name__}")
                return result
            
            except ValueError as ve:
                logger.error(f"Input validation failed for {func.__name__}: {ve}")
                raise
            except TypeError as te:
                logger.error(f"Invalid input type for {func.__name__}: {te}")
                raise
        
        return wrapper
    
    return decorator