import time
import functools
import logging

def log_execution_time(logger=None):
    """
    A decorator to log the execution time of a function.
    
    Args:
        logger (logging.Logger, optional): Logger to use for recording execution time. 
                                           If not provided, uses basic print logging.
    
    Returns:
        callable: Decorated function that logs its execution time
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Start timing
            start_time = time.time()
            
            try:
                # Execute the original function
                result = func(*args, **kwargs)
                
                # Calculate execution time
                execution_time = time.time() - start_time
                
                # Log the execution time
                log_message = f"Function '{func.__name__}' executed in {execution_time:.4f} seconds"
                if logger:
                    logger.info(log_message)
                else:
                    print(log_message)
                
                return result
            
            except Exception as e:
                # Log any exceptions that occur
                execution_time = time.time() - start_time
                error_message = f"Function '{func.__name__}' raised an exception after {execution_time:.4f} seconds: {str(e)}"
                if logger:
                    logger.error(error_message)
                else:
                    print(f"Error: {error_message}")
                raise
        
        return wrapper
    return decorator