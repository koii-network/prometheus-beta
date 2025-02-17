import functools
import logging
import psutil
import os

def log_memory_usage(logger=None):
    """
    A decorator to log memory usage before and after a function call.
    
    :param logger: Optional logger. If not provided, uses root logger.
    :return: Decorator function
    """
    if logger is None:
        logger = logging.getLogger()
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Get initial memory usage
            process = psutil.Process(os.getpid())
            initial_memory = process.memory_info().rss / 1024 / 1024  # Convert to MB
            
            logger.info(f"Before {func.__name__}: Memory usage = {initial_memory:.2f} MB")
            
            # Call the original function
            result = func(*args, **kwargs)
            
            # Get memory usage after function call
            final_memory = process.memory_info().rss / 1024 / 1024  # Convert to MB
            memory_diff = final_memory - initial_memory
            
            logger.info(f"After {func.__name__}: Memory usage = {final_memory:.2f} MB")
            logger.info(f"Memory change: {memory_diff:.2f} MB")
            
            return result
        return wrapper
    return decorator