import time
import functools
import logging
from typing import Callable, Any

def log_query_time(logger: logging.Logger = None):
    """
    Decorator to log database query execution times.
    
    Args:
        logger (logging.Logger, optional): Logger to use for recording query times. 
                Defaults to a standard logger if not provided.
    
    Returns:
        Decorator function that logs query execution time
    """
    # Create a default logger if none is provided
    if logger is None:
        logger = logging.getLogger(__name__)
        # Ensure basic logging configuration if not set
        if not logger.handlers:
            logging.basicConfig(level=logging.INFO, 
                                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        """
        Decorator that wraps the function to log its execution time.
        
        Args:
            func (Callable): The database query function to be logged
        
        Returns:
            Wrapped function with timing and logging
        """
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """
            Wrapper function that measures and logs query execution time.
            
            Returns:
                Result of the original function
            """
            # Start timing
            start_time = time.perf_counter()
            
            try:
                # Execute the original function
                result = func(*args, **kwargs)
                
                # Calculate execution time
                end_time = time.perf_counter()
                execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
                
                # Log the execution time
                logger.info(f"Query '{func.__name__}' executed in {execution_time:.2f} ms")
                
                return result
            
            except Exception as e:
                # Log any exceptions that occur during query execution
                logger.error(f"Error in query '{func.__name__}': {str(e)}")
                raise
        
        return wrapper
    
    return decorator