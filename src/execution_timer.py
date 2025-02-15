import time
import functools
from typing import Callable, Any

def measure_execution_time(func: Callable[..., Any]) -> Callable[..., tuple]:
    """
    A decorator that measures the execution time of a function.
    
    Args:
        func (Callable): The function to measure execution time for.
    
    Returns:
        Callable: A wrapped function that returns a tuple of (original_result, execution_time)
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Record start time
        start_time = time.perf_counter()
        
        # Execute the function
        result = func(*args, **kwargs)
        
        # Calculate execution time
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        
        # Return a tuple of (original result, execution time)
        return result, execution_time
    
    return wrapper