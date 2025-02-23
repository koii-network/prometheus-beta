import time
import functools
import logging
from typing import Callable, Any

def log_query_execution_time(logger: logging.Logger = None):
    """
    Decorator to log database query execution times.
    
    Args:
        logger (logging.Logger, optional): Logger to use for recording query times. 
                If not provided, uses the root logger.
    
    Returns:
        Callable: Decorated function that logs execution time of the database query.
    """
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Use provided logger or root logger
            log = logger or logging.getLogger()
            
            # Start timing
            start_time = time.perf_counter()
            
            try:
                # Execute the query
                result = func(*args, **kwargs)
                
                # Calculate execution time
                end_time = time.perf_counter()
                execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
                
                # Log the execution time
                log.info(f"Query '{func.__name__}' executed in {execution_time:.2f} ms")
                
                return result
            
            except Exception as e:
                # Log any exceptions that occur during query execution
                log.error(f"Error in query '{func.__name__}': {str(e)}")
                raise
        
        return wrapper
    
    return decorator