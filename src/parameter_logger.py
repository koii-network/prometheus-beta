import functools
import logging
import inspect

def log_params(logger=None):
    """
    A decorator that logs function parameters on invocation.
    
    Args:
        logger (logging.Logger, optional): A custom logger. 
                If not provided, uses the root logger.
    
    Returns:
        Decorator function that logs parameters
    """
    if logger is None:
        logger = logging.getLogger()
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Get the signature of the function
            sig = inspect.signature(func)
            
            # Bind the arguments to the function's parameters
            bound_arguments = sig.bind(*args, **kwargs)
            bound_arguments.apply_defaults()
            
            # Log the function name and its parameters
            logger.info(f"Calling function: {func.__name__}")
            for param_name, param_value in bound_arguments.arguments.items():
                logger.info(f"Parameter '{param_name}': {param_value}")
            
            # Call the original function
            return func(*args, **kwargs)
        return wrapper
    return decorator