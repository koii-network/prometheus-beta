import functools
import logging
import time

def log_execution(logger=None):
    """
    A decorator to log function execution start and end with optional custom logger.
    
    Args:
        logger (logging.Logger, optional): Custom logger. If not provided, uses root logger.
    
    Returns:
        Decorator function that logs function entry, exit, and execution time.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Use provided logger or root logger
            log = logger or logging.getLogger()
            
            # Log function entry
            log.info(f"Entering function: {func.__name__}")
            log.info(f"Args: {args}, Kwargs: {kwargs}")
            
            # Record start time
            start_time = time.time()
            
            try:
                # Execute the function
                result = func(*args, **kwargs)
                
                # Calculate execution time
                end_time = time.time()
                execution_time = end_time - start_time
                
                # Log successful completion
                log.info(f"Exiting function: {func.__name__}")
                log.info(f"Execution time: {execution_time:.4f} seconds")
                
                return result
            
            except Exception as e:
                # Log any exceptions
                log.error(f"Exception in {func.__name__}: {str(e)}")
                raise
        
        return wrapper
    return decorator