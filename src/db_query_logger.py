import time
import functools
import logging
from typing import Callable, Any

def log_query_execution_time(logger: logging.Logger = None) -> Callable:
    """
    A decorator to log the execution time of database queries.

    Args:
        logger (logging.Logger, optional): Logger to use for recording query times. 
                                           If not provided, uses the root logger.

    Returns:
        Callable: Decorated function that logs execution time.

    Raises:
        TypeError: If the decorated function is not callable.
    """
    if logger is None:
        logger = logging.getLogger()

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time = time.perf_counter()
            try:
                result = func(*args, **kwargs)
                end_time = time.perf_counter()
                execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
                
                logger.info(
                    f"Query '{func.__name__}' executed in {execution_time:.2f} ms"
                )
                return result
            except Exception as e:
                end_time = time.perf_counter()
                execution_time = (end_time - start_time) * 1000
                
                logger.error(
                    f"Query '{func.__name__}' failed after {execution_time:.2f} ms: {str(e)}"
                )
                raise
        return wrapper
    return decorator