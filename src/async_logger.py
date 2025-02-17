import asyncio
import time
import functools
import logging

def log_async_execution_time(logger=None):
    """
    Decorator to log the execution time of asynchronous functions.
    
    Args:
        logger (logging.Logger, optional): Logger to use. If not provided, 
                                           uses the root logger.
    
    Returns:
        Decorator that logs the execution time of the async function.
    """
    if logger is None:
        logger = logging.getLogger()
    
    def decorator(func):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            # Record start time
            start_time = time.perf_counter()
            
            try:
                # Execute the async function
                result = await func(*args, **kwargs)
                
                # Calculate execution time
                end_time = time.perf_counter()
                execution_time = end_time - start_time
                
                # Log the execution time
                logger.info(
                    f"Async function '{func.__name__}' "
                    f"executed in {execution_time:.4f} seconds"
                )
                
                return result
            
            except Exception as e:
                # Log any exceptions that occur
                end_time = time.perf_counter()
                execution_time = end_time - start_time
                logger.error(
                    f"Async function '{func.__name__}' "
                    f"failed after {execution_time:.4f} seconds: {str(e)}"
                )
                raise
        
        return wrapper
    
    return decorator