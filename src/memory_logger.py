import functools
import logging
import memory_profiler

def log_memory_usage(logger=None):
    """
    A decorator to log memory usage before and after a function call.
    
    Args:
        logger (logging.Logger, optional): Logger to use. If None, creates a default logger.
    
    Returns:
        callable: Decorated function that logs memory usage
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Use default logger if not provided
            nonlocal logger
            if logger is None:
                logger = logging.getLogger(func.__module__)
                logger.setLevel(logging.INFO)
                
                # Create console handler if no handlers exist
                if not logger.handlers:
                    console_handler = logging.StreamHandler()
                    console_handler.setLevel(logging.INFO)
                    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
                    console_handler.setFormatter(formatter)
                    logger.addHandler(console_handler)
            
            # Log memory before function call
            mem_before = memory_profiler.memory_usage()[0]
            logger.info(f"Memory before {func.__name__}: {mem_before} MiB")
            
            # Execute the function
            result = func(*args, **kwargs)
            
            # Log memory after function call
            mem_after = memory_profiler.memory_usage()[0]
            logger.info(f"Memory after {func.__name__}: {mem_after} MiB")
            logger.info(f"Memory change in {func.__name__}: {mem_after - mem_before} MiB")
            
            return result
        return wrapper
    return decorator