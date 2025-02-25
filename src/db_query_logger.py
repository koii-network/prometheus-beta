import logging
import time
import functools
from typing import Callable, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def log_query_time(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    A decorator to log database query execution times.
    
    Args:
        func (Callable): The database query function to be logged.
    
    Returns:
        Callable: Wrapped function with execution time logging.
    
    Raises:
        Exception: Propagates any exceptions from the original function.
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Start timing
        start_time = time.perf_counter()
        
        try:
            # Execute the original function
            result = func(*args, **kwargs)
            
            # Calculate and log execution time
            end_time = time.perf_counter()
            execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
            
            logger.info(
                f"Query '{func.__name__}' executed in {execution_time:.2f} ms"
            )
            
            return result
        
        except Exception as e:
            # Log any exceptions that occur during query execution
            logger.error(
                f"Error in query '{func.__name__}': {str(e)}"
            )
            raise
    
    return wrapper