import time
from functools import wraps

def measure_execution_time(func):
    """
    A decorator that measures and returns the execution time of a function.
    
    Args:
        func (callable): The function to measure.
    
    Returns:
        callable: A wrapped function that returns a tuple of (original_result, execution_time)
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        return result, execution_time
    
    return wrapper