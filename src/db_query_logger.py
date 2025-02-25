import logging
import time
import functools
from typing import Callable, Any, Optional

def log_query_time(logger: Optional[logging.Logger] = None) -> Callable:
    """
    A decorator to log database query execution times.
    
    Args:
        logger (Optional[logging.Logger]): Logger to use. 
                If None, uses the default root logger.
    
    Returns:
        Callable: Decorator for logging query execution times.
    """
    # Use default logger if not provided
    if logger is None:
        logger = logging.getLogger(__name__)
    
    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
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
    
    return decorator