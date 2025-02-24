import functools
import logging
import inspect

def log_parameters(logger=None):
    """
    A decorator that logs function parameters on invocation.
    
    Args:
        logger (logging.Logger, optional): A specific logger to use. 
                If not provided, uses the root logger.
    
    Returns:
        callable: A decorator function that logs parameters before function execution.
    """
    # Use root logger if no specific logger is provided
    if logger is None:
        logger = logging.getLogger()
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Get the function signature
            sig = inspect.signature(func)
            
            # Bind the arguments to the signature to get a mapping of parameter names to values
            bound_arguments = sig.bind(*args, **kwargs)
            bound_arguments.apply_defaults()
            
            # Create a dictionary of parameter names and their values
            param_dict = dict(bound_arguments.arguments)
            
            # Log the function name and its parameters
            logger.info(f"Calling function: {func.__name__}")
            for param, value in param_dict.items():
                logger.info(f"  Parameter '{param}': {repr(value)}")
            
            # Call the original function
            return func(*args, **kwargs)
        return wrapper
    return decorator