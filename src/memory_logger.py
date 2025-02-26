import functools
import logging
import os
import psutil

def log_memory_usage(func):
    """
    A decorator that logs memory usage before and after a function call.
    
    Args:
        func (callable): The function to be wrapped and monitored.
    
    Returns:
        callable: The wrapped function with memory logging.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Get current process
        process = psutil.Process(os.getpid())
        
        # Log memory before function call
        memory_before = process.memory_info().rss / (1024 * 1024)  # Convert to MB
        logging.info(f"Memory usage before {func.__name__}: {memory_before:.2f} MB")
        
        # Call the original function
        result = func(*args, **kwargs)
        
        # Log memory after function call
        memory_after = process.memory_info().rss / (1024 * 1024)  # Convert to MB
        logging.info(f"Memory usage after {func.__name__}: {memory_after:.2f} MB")
        
        # Calculate and log memory difference
        memory_diff = memory_after - memory_before
        logging.info(f"Memory change during {func.__name__}: {memory_diff:.2f} MB")
        
        return result
    
    return wrapper