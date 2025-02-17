import time
import logging
from functools import wraps

def log_query_execution_time(logger=None):
    """
    Decorator to log the execution time of database queries.
    
    :param logger: Optional custom logger. If not provided, uses Python's default logging.
    :return: Decorated function that logs query execution time
    """
    if logger is None:
        logger = logging.getLogger(__name__)
        # Configure basic logging if no logger is provided
        logging.basicConfig(level=logging.INFO, 
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
                end_time = time.time()
                execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
                
                # Log query details
                logger.info(f"Query '{func.__name__}' executed in {execution_time:.2f} ms")
                
                return result
            except Exception as e:
                end_time = time.time()
                execution_time = (end_time - start_time) * 1000
                logger.error(f"Query '{func.__name__}' failed after {execution_time:.2f} ms: {str(e)}")
                raise
        return wrapper
    return decorator