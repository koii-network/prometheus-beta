import functools
import logging
import psutil
import os

def log_memory_usage(func):
    """
    A decorator that logs memory usage before and after function execution.
    
    Args:
        func (callable): The function to be decorated.
    
    Returns:
        callable: Wrapped function with memory logging.
    
    Raises:
        TypeError: If the input is not a callable.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Validate input
        if not callable(func):
            raise TypeError("Decorator can only be applied to callable objects")
        
        # Set up logging
        logger = logging.getLogger(func.__module__)
        logger.setLevel(logging.INFO)
        
        # Create log handler if not exists
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        
        # Get memory before function call
        process = psutil.Process(os.getpid())
        memory_before = process.memory_info().rss / (1024 * 1024)  # Convert to MB
        
        logger.info(f"Memory before {func.__name__}: {memory_before:.2f} MB")
        
        try:
            # Execute the function
            result = func(*args, **kwargs)
            
            # Get memory after function call
            memory_after = process.memory_info().rss / (1024 * 1024)  # Convert to MB
            memory_diff = memory_after - memory_before
            
            logger.info(f"Memory after {func.__name__}: {memory_after:.2f} MB")
            logger.info(f"Memory change: {memory_diff:.2f} MB")
            
            return result
        
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {str(e)}")
            raise
    
    return wrapper