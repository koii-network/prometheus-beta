import functools
import logging
import time
from typing import Callable, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)

def log_execution_time(func: Callable) -> Callable:
    """
    A decorator that logs the start and end of function execution,
    including execution time.

    Args:
        func (Callable): The function to be decorated.

    Returns:
        Callable: Wrapped function with logging functionality.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Log function start
        logger.info(f"Starting execution of {func.__name__}")
        logger.info(f"Arguments: args={args}, kwargs={kwargs}")
        
        # Record start time
        start_time = time.time()
        
        try:
            # Execute the original function
            result = func(*args, **kwargs)
            
            # Calculate and log execution time
            end_time = time.time()
            execution_time = end_time - start_time
            
            logger.info(f"Finished execution of {func.__name__}")
            logger.info(f"Execution time: {execution_time:.4f} seconds")
            
            return result
        
        except Exception as e:
            # Log any exceptions that occur
            logger.error(f"Exception in {func.__name__}: {str(e)}")
            raise
    
    return wrapper