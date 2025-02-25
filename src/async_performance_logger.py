import asyncio
import time
import functools
import logging
from typing import Callable, Any, Coroutine

# Configure logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def log_async_execution_time(logger_obj: logging.Logger = logger) -> Callable:
    """
    A decorator to log execution times of asynchronous functions.
    
    Args:
        logger_obj (logging.Logger, optional): Logger to use for recording times. 
                                               Defaults to module-level logger.
    
    Returns:
        Callable: A decorator that logs async function execution times.
    
    Example:
        @log_async_execution_time()
        async def example_async_func():
            await asyncio.sleep(1)
    """
    def decorator(func: Callable[..., Coroutine[Any, Any, Any]]) -> Callable:
        @functools.wraps(func)
        async def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Capture start time
            start_time = time.perf_counter()
            
            try:
                # Execute the async function
                result = await func(*args, **kwargs)
                
                # Calculate and log execution time
                end_time = time.perf_counter()
                execution_time = end_time - start_time
                
                logger_obj.info(
                    f"Async function '{func.__name__}' executed in {execution_time:.4f} seconds"
                )
                
                return result
            
            except Exception as e:
                # Log any exceptions that occur during async execution
                end_time = time.perf_counter()
                execution_time = end_time - start_time
                
                logger_obj.error(
                    f"Async function '{func.__name__}' failed after {execution_time:.4f} seconds. "
                    f"Error: {str(e)}"
                )
                raise
        
        return wrapper
    
    return decorator