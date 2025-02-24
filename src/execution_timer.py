import time
import functools
import logging

def log_execution_time(logger=None):
    """
    A decorator to log the execution time of a function.

    Args:
        logger (logging.Logger, optional): A logger to use for recording 
                                           execution time. If None, uses 
                                           basic print logging.

    Returns:
        callable: A decorator that logs function execution time.
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
                if logger:
                    logger.info(f"Function '{func.__name__}' took {execution_time:.4f} seconds to execute.")
                else:
                    print(f"Function '{func.__name__}' took {execution_time:.4f} seconds to execute.")
                
                return result
            
            except Exception as e:
                # Log any exceptions that occur
                if logger:
                    logger.error(f"Error in function '{func.__name__}': {str(e)}")
                else:
                    print(f"Error in function '{func.__name__}': {str(e)}")
                raise
        
        return wrapper
    
    return decorator