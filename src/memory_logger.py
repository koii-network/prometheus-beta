import functools
import logging
import memory_profiler

def log_memory_usage(logger=None):
    """
    A decorator that logs memory usage before and after a function call.
    
    :param logger: Optional logger. If not provided, uses basic print logging.
    :return: Decorator function
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Get initial memory usage
            initial_memory = memory_profiler.memory_usage()[0]
            
            # Log initial memory if logger is provided
            if logger:
                logger.info(f"Memory before {func.__name__}: {initial_memory} MiB")
            else:
                print(f"Memory before {func.__name__}: {initial_memory} MiB")
            
            # Call the original function
            result = func(*args, **kwargs)
            
            # Get final memory usage
            final_memory = memory_profiler.memory_usage()[0]
            
            # Log final memory and difference
            memory_diff = final_memory - initial_memory
            if logger:
                logger.info(f"Memory after {func.__name__}: {final_memory} MiB")
                logger.info(f"Memory change: {memory_diff} MiB")
            else:
                print(f"Memory after {func.__name__}: {final_memory} MiB")
                print(f"Memory change: {memory_diff} MiB")
            
            return result
        return wrapper
    return decorator