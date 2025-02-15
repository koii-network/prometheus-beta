import functools
import logging
import inspect

def log_parameters(logger=None):
    """
    A decorator that logs function parameters on invocation.
    
    :param logger: Optional custom logger. If not provided, uses root logger.
    :return: Decorated function that logs its parameters
    """
    if logger is None:
        logger = logging.getLogger()
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Get the function signature
            sig = inspect.signature(func)
            
            # Bind the arguments to the function's parameters
            bound_arguments = sig.bind(*args, **kwargs)
            bound_arguments.apply_defaults()
            
            # Convert bound arguments to a dictionary
            arg_dict = bound_arguments.arguments
            
            # Log the function name and its parameters
            logger.info(f"Calling function: {func.__name__}")
            for param_name, param_value in arg_dict.items():
                logger.info(f"  Parameter '{param_name}': {repr(param_value)}")
            
            # Call the original function
            return func(*args, **kwargs)
        return wrapper
    return decorator