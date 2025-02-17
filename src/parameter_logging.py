import functools
import logging
import inspect

def log_parameters(logger=None):
    """
    A decorator that logs function parameters on invocation.
    
    :param logger: Optional logger. If not provided, uses the root logger.
    :return: Decorator function
    """
    if logger is None:
        logger = logging.getLogger()
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Get the function signature
            sig = inspect.signature(func)
            bound_arguments = sig.bind(*args, **kwargs)
            bound_arguments.apply_defaults()
            
            # Create a log message with function name and parameters
            params_str = ", ".join([
                f"{name}={repr(value)}" 
                for name, value in bound_arguments.arguments.items()
            ])
            
            logger.info(f"Calling {func.__name__}({params_str})")
            
            # Call the original function
            return func(*args, **kwargs)
        return wrapper
    return decorator