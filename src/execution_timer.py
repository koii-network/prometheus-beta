import time
import functools
import logging

def log_execution_time(logger=None):
    """
    A decorator that logs the execution time of a function.
    
    Args:
        logger (logging.Logger, optional): A logger to use for logging. 
                If not provided, uses the root logger.
    
    Returns:
        Decorator function that logs execution time
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Use provided logger or root logger
            log = logger or logging.getLogger()
            
            # Start timing
            start_time = time.time()
            
            try:
                # Execute the function
                result = func(*args, **kwargs)
                
                # Calculate execution time
                end_time = time.time()
                execution_time = end_time - start_time
                
                # Log the execution time
                log.info(f"Function '{func.__name__}' took {execution_time:.4f} seconds to execute")
                
                return result
            
            except Exception as e:
                # Log any exceptions that occur
                log.error(f"Error in function '{func.__name__}': {str(e)}")
                raise
        
        return wrapper
    return decorator