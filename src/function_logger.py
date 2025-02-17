import functools
import logging
import time

def log_execution(logger=None):
    """
    A decorator to log function execution start and end times.
    
    :param logger: Optional logger. If not provided, uses the root logger.
    :return: Decorator function
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Use provided logger or root logger
            log = logger or logging.getLogger()
            
            # Log function start
            log.info(f"Executing function: {func.__name__}")
            log.info(f"Arguments: args={args}, kwargs={kwargs}")
            
            # Record start time
            start_time = time.time()
            
            try:
                # Execute the function
                result = func(*args, **kwargs)
                
                # Calculate execution time
                end_time = time.time()
                execution_time = end_time - start_time
                
                # Log function end and result
                log.info(f"Function {func.__name__} completed successfully")
                log.info(f"Execution time: {execution_time:.4f} seconds")
                
                return result
            
            except Exception as e:
                # Log any exceptions
                log.error(f"Exception in function {func.__name__}: {str(e)}")
                raise
        
        return wrapper
    return decorator