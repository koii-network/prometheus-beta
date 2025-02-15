import asyncio
import time
import logging
from functools import wraps

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_async_execution_time(logger=logging.getLogger(__name__)):
    """
    Decorator to log execution time of asynchronous functions.
    
    Args:
        logger (logging.Logger, optional): Logger to use. Defaults to module-level logger.
    
    Returns:
        Decorator function that logs execution time of async functions.
    """
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                result = await func(*args, **kwargs)
                end_time = time.time()
                execution_time = end_time - start_time
                logger.info(f"Async function '{func.__name__}' executed in {execution_time:.4f} seconds")
                return result
            except Exception as e:
                end_time = time.time()
                execution_time = end_time - start_time
                logger.error(f"Async function '{func.__name__}' failed after {execution_time:.4f} seconds: {str(e)}")
                raise
        return wrapper
    return decorator