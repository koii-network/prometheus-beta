import time
import logging
from functools import wraps

def log_query_execution_time(logger=None):
    """
    A decorator to log database query execution times.
    
    :param logger: Optional logger. If not provided, uses the root logger.
    :return: Decorated function that logs query execution time
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
                
                # Log the query execution time
                logger.info(f"Query '{func.__name__}' executed in {execution_time:.4f} seconds")
                
                return result
            except Exception as e:
                end_time = time.time()
                execution_time = end_time - start_time
                
                # Log any exceptions along with execution time
                logger.error(f"Query '{func.__name__}' failed after {execution_time:.4f} seconds. Error: {str(e)}")
                raise
        return wrapper
    return decorator