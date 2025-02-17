import functools
import logging
import inspect

def log_parameters(logger=None):
    """
    A decorator that logs function parameters on invocation.
    
    :param logger: Optional logger. If not provided, uses the root logger.
    :return: Decorator function
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Use provided logger or get root logger
            log = logger or logging.getLogger()
            
            # Get the function's signature
            sig = inspect.signature(func)
            
            # Bind the arguments to the function's parameters
            bound_arguments = sig.bind(*args, **kwargs)
            bound_arguments.apply_defaults()
            
            # Create a log message with function name and parameters
            log_message = f"Calling {func.__name__} with parameters:"
            for param_name, param_value in bound_arguments.arguments.items():
                log_message += f"\n  {param_name}: {repr(param_value)}"
            
            # Log the parameter information
            log.info(log_message)
            
            # Call the original function
            return func(*args, **kwargs)
        return wrapper
    return decorator