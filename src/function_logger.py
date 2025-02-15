import functools
import logging
import time
from typing import Callable, Any

def log_execution(logger: logging.Logger = None):
    """
    A decorator to log function execution start and end.
    
    Args:
        logger (logging.Logger, optional): Logger to use. If not provided, 
                                           uses the root logger.
    
    Returns:
        Callable: Decorated function with logging
    """
    if logger is None:
        logger = logging.getLogger()
    
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Generate log message with function name
            func_name = func.__name__
            
            # Log function start
            logger.info(f"Starting execution of {func_name}")
            logger.debug(f"Arguments: args={args}, kwargs={kwargs}")
            
            # Record start time
            start_time = time.time()
            
            try:
                # Execute the function
                result = func(*args, **kwargs)
                
                # Calculate execution time
                execution_time = time.time() - start_time
                
                # Log function end and result
                logger.info(f"Finished execution of {func_name}")
                logger.debug(f"Execution time: {execution_time:.4f} seconds")
                logger.debug(f"Return value: {result}")
                
                return result
            
            except Exception as e:
                # Log any exceptions
                logger.error(f"Exception in {func_name}: {str(e)}")
                raise
        
        return wrapper
    
    return decorator