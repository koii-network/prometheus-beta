import asyncio
import time
import functools
import logging
from typing import Callable, Any, Awaitable

def log_async_execution_time(logger: logging.Logger = None):
    """
    A decorator to log execution times of asynchronous functions.
    
    :param logger: Optional logger. If not provided, uses the root logger.
    :return: Decorator function
    """
    if logger is None:
        logger = logging.getLogger()
    
    def decorator(func: Callable[..., Awaitable[Any]]):
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
                
                logger.error(f"Async function '{func.__name__}' failed after {execution_time:.4f} seconds: {str(e)}")
                raise
        
        return wrapper
    
    return decorator