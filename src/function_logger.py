import functools
import logging
import time
from typing import Callable, Any

def log_function_execution(logger: logging.Logger = None):
    """
    A decorator that logs the start and end of function execution.
    
    Args:
        logger (logging.Logger, optional): Logger to use. If not provided, 
                                           uses the root logger.
    
    Returns:
        Callable: Decorated function that logs execution details
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Use provided logger or root logger
            log = logger or logging.getLogger()
            
            # Log function start
            log.info(f"Starting execution of {func.__name__}")
            log.debug(f"Args: {args}, Kwargs: {kwargs}")
            
            # Record start time
            start_time = time.time()
            
            try:
                # Execute the function
                result = func(*args, **kwargs)
                
                # Calculate execution time
                end_time = time.time()
                execution_time = end_time - start_time
                
                # Log successful completion
                log.info(f"Finished execution of {func.__name__}")
                log.info(f"Execution time: {execution_time:.4f} seconds")
                
                return result
            
            except Exception as e:
                # Log any exceptions
                log.error(f"Exception in {func.__name__}: {str(e)}")
                raise
        
        return wrapper
    
    return decorator