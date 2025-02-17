import time
from functools import wraps

def measure_execution_time(func):
    """
    A decorator that measures and returns the execution time of a function.
    
    Args:
        func (callable): The function to measure execution time for.
    
    Returns:
        A wrapped function that returns a tuple of (original_return_value, execution_time_in_seconds)
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        return result, execution_time
    
    return wrapper