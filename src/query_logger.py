import time
import logging
import functools

logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def log_query_time(func):
    """
    A decorator to log the execution time of database queries.
    
    Args:
        func (callable): The database query function to be wrapped.
    
    Returns:
        callable: A wrapped function that logs execution time.
    
    Raises:
        TypeError: If the decorated function is not callable.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Validate input
        if not callable(func):
            raise TypeError("Decorator must be applied to a callable function")
        
        # Start timing
        start_time = time.time()
        
        try:
            # Execute the original function
            result = func(*args, **kwargs)
            
            # Calculate execution time
            end_time = time.time()
            execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
            
            # Log the execution time
            logger.info(f"Query '{func.__name__}' executed in {execution_time:.2f} ms")
            
            return result
        
        except Exception as e:
            # Log any exceptions that occur during query execution
            logger.error(f"Error in query '{func.__name__}': {str(e)}")
            raise
    
    return wrapper