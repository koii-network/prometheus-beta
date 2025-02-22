import functools
import logging
import memory_profiler

def log_memory_usage(logger=None):
    """
    A decorator to log memory usage before and after a function call.
    
    :param logger: Optional logger. If not provided, uses the root logger.
    :return: Decorator function
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Use the provided logger or the root logger
            log = logger or logging.getLogger()
            
            # Get memory usage before function call
            memory_before = memory_profiler.memory_usage()[0]
            log.info(f"Memory usage before {func.__name__}: {memory_before} MiB")
            
            # Execute the function
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                # Log any exceptions that occur
                log.error(f"Error in {func.__name__}: {e}")
                raise
            
            # Get memory usage after function call
            memory_after = memory_profiler.memory_usage()[0]
            log.info(f"Memory usage after {func.__name__}: {memory_after} MiB")
            
            # Calculate and log memory difference
            memory_diff = memory_after - memory_before
            log.info(f"Memory usage change in {func.__name__}: {memory_diff} MiB")
            
            return result
        return wrapper
    return decorator