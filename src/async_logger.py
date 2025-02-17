import asyncio
import time
import functools
import logging

def log_async_execution_time(logger=None):
    """
    A decorator to log the execution time of asynchronous functions.
    
    :param logger: Optional custom logger. If not provided, uses the root logger.
    :return: Decorator function that logs execution time
    """
    if logger is None:
        logger = logging.getLogger()
    
    def decorator(func):
        @functools.wraps(func)
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
                logger.error(f"Async function '{func.__name__}' failed after {execution_time:.4f} seconds. Error: {str(e)}")
                raise
        return wrapper
    return decorator