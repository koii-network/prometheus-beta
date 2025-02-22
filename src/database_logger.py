import time
import functools
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def log_query_time(func):
    """
    A decorator to log the execution time of database queries.
    
    Args:
        func (callable): The database query function to be decorated.
    
    Returns:
        callable: A wrapped function that logs query execution time.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        try:
            result = func(*args, **kwargs)
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
            
            # Log query details
            query_details = f"Query: {func.__name__}, Execution Time: {execution_time:.2f} ms"
            logger.info(query_details)
            
            return result
        except Exception as e:
            logger.error(f"Error in query {func.__name__}: {str(e)}")
            raise
    return wrapper