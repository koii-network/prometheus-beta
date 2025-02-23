import time
import functools
import logging
from typing import Callable, Any

def log_query_time(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    A decorator to log the execution time of database query functions.
    
    Args:
        func (Callable): The database query function to be decorated.
    
    Returns:
        Callable: A wrapped function that logs execution time.
    
    Raises:
        TypeError: If the input is not a callable function.
    """
    # Validate input is a callable before anything else
    if not callable(func):
        raise TypeError("Input must be a callable function")
    
    # Get logger for the module where the decorated function is defined
    logger = logging.getLogger(func.__module__)
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Start timing
        start_time = time.perf_counter()
        
        try:
            # Execute the original function
            result = func(*args, **kwargs)
            
            # Calculate and log execution time
            end_time = time.perf_counter()
            execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
            
            logger.info(f"Query '{func.__name__}' executed in {execution_time:.2f} ms")
            
            return result
        
        except Exception as e:
            # Log any exceptions that occur during query execution
            logger.error(f"Error in query '{func.__name__}': {str(e)}")
            raise
    
    return wrapper