import functools
import logging
import inspect

def log_parameters(logger=None):
    """
    A decorator that logs function parameters on invocation.
    
    Args:
        logger (logging.Logger, optional): Logger to use. 
                If not provided, uses the root logger.
    
    Returns:
        Decorator function that logs parameters of the wrapped function.
    
    Example:
        @log_parameters()
        def example_func(a, b, c=None):
            pass
    """
    # If no logger is provided, use root logger and ensure it's set to at least INFO level
    if logger is None:
        logger = logging.getLogger()
        # Ensure at least INFO level is set
        if logger.level > logging.INFO:
            logger.setLevel(logging.INFO)
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Get the function signature
            sig = inspect.signature(func)
            
            # Bind the arguments to the signature to get their names
            bound_arguments = sig.bind(*args, **kwargs)
            bound_arguments.apply_defaults()
            
            # Create a dictionary of all parameters
            params = bound_arguments.arguments
            
            # Log the function name and its parameters
            logger.info(f"Calling {func.__name__} with parameters: {params}")
            
            # Call the original function
            return func(*args, **kwargs)
        return wrapper
    return decorator