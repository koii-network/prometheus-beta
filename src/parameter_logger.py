import functools
import logging
import inspect

def log_parameters(logger=None):
    """
    A decorator that logs function parameters on invocation.
    
    Args:
        logger (logging.Logger, optional): A custom logger. 
                If not provided, uses the root logger.
    
    Returns:
        callable: A decorator function that logs parameters
    
    Example:
        @log_parameters()
        def example_function(a, b, c=10):
            pass
    """
    # Use root logger if no logger is provided
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
            
            # Create a dictionary of parameter names and their values
            params_dict = bound_arguments.arguments
            
            # Log the function name and its parameters
            logger.info(f"Calling {func.__name__} with parameters: {params_dict}")
            
            # Call the original function
            return func(*args, **kwargs)
        
        return wrapper
    
    return decorator