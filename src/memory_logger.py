import functools
import psutil
import logging
import sys

def log_memory_usage(logger=None):
    """
    A decorator that logs memory usage before and after a function call.
    
    Args:
        logger (logging.Logger, optional): Logger to use for memory logging. 
                If None, creates a default logger.
    
    Returns:
        Decorator function that wraps the original function with memory logging.
    """
    # Create a default logger if none is provided
    if logger is None:
        # Use the root logger with a stream handler configured to sys.stdout
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        
        # Remove existing handlers to prevent duplicate log messages
        logger.handlers.clear()
        
        # Create a new stream handler
        handler = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Get memory usage before function call
            process = psutil.Process()
            memory_before = process.memory_info().rss / (1024 * 1024)  # Convert to MB
            
            # Log memory before function call
            logger.info(f"Memory before {func.__name__}: {memory_before:.2f} MB")
            
            try:
                # Execute the function
                result = func(*args, **kwargs)
                
                # Get memory usage after function call
                memory_after = process.memory_info().rss / (1024 * 1024)  # Convert to MB
                
                # Log memory after function call
                logger.info(f"Memory after {func.__name__}: {memory_after:.2f} MB")
                
                # Log memory difference
                memory_diff = memory_after - memory_before
                logger.info(f"Memory change for {func.__name__}: {memory_diff:.2f} MB")
                
                return result
            
            except Exception as e:
                # Log any exceptions that occur
                logger.error(f"Error in {func.__name__}: {str(e)}")
                raise
        
        return wrapper
    
    return decorator