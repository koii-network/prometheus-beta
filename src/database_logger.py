import time
import logging
from functools import wraps

def log_query_execution_time(logger=None):
    """
    Decorator to log database query execution times.
    
    Args:
        logger (logging.Logger, optional): Logger to use. 
                If not provided, uses the root logger.
    
    Returns:
        Decorator function that logs query execution time
    """
    if logger is None:
        logger = logging.getLogger()
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
                end_time = time.time()
                execution_time = end_time - start_time
                
                # Log query details
                logger.info(
                    f"Query: {func.__name__} | "
                    f"Execution Time: {execution_time:.4f} seconds"
                )
                
                return result
            except Exception as e:
                end_time = time.time()
                execution_time = end_time - start_time
                
                # Log error with execution time
                logger.error(
                    f"Query: {func.__name__} | "
                    f"Execution Time: {execution_time:.4f} seconds | "
                    f"Error: {str(e)}"
                )
                raise
        return wrapper
    return decorator