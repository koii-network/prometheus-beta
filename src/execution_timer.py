import time
import functools
from typing import Callable, Any, TypeVar

T = TypeVar('T')

def measure_execution_time(func: Callable[..., T]) -> Callable[..., tuple[T, float]]:
    """
    A decorator that measures the execution time of a function.
    
    Args:
        func (Callable): The function to measure execution time for.
    
    Returns:
        Callable: A wrapped function that returns a tuple of:
            - The original function's return value
            - Execution time in seconds
    
    Raises:
        TypeError: If the input is not a callable
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> tuple[T, float]:
        # Validate input is callable
        if not callable(func):
            raise TypeError("Input must be a callable function")
        
        # Measure start time
        start_time = time.perf_counter()
        
        # Execute the function
        result = func(*args, **kwargs)
        
        # Measure end time and calculate duration
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        
        return result, execution_time
    
    return wrapper