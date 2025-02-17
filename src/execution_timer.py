import time
import functools
import logging

def log_execution_time(logger=None):
    """
    A decorator to log the execution time of a function.
    
    Args:
        logger (logging.Logger, optional): Logger to use. If not provided, 
                                           defaults to printing to console.
    
    Returns:
        callable: Decorated function that logs execution time
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Start timing
            start_time = time.time()
            
            # Execute the original function
            result = func(*args, **kwargs)
            
            # Calculate execution time
            end_time = time.time()
            execution_time = end_time - start_time
            
            # Log the execution time
            log_message = f"Function '{func.__name__}' took {execution_time:.4f} seconds to execute"
            
            if logger:
                logger.info(log_message)
            else:
                print(log_message)
            
            return result
        return wrapper
    return decorator

# Example usage
@log_execution_time()
def example_function(x, y):
    """
    A simple example function to demonstrate execution time logging.
    
    Args:
        x (int): First number
        y (int): Second number
    
    Returns:
        int: Sum of x and y after a small delay
    """
    time.sleep(0.5)  # Simulate some work
    return x + y