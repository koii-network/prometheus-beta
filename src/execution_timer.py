import time
from functools import wraps
from typing import Callable, Any


def measure_execution_time(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    A decorator that measures and prints the execution time of a function.
    
    Args:
        func (Callable): The function whose execution time is to be measured.
    
    Returns:
        Callable: A wrapped function that prints its execution time.
    
    Example:
        @measure_execution_time
        def example_function(x, y):
            time.sleep(1)
            return x + y
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Record start time
        start_time = time.perf_counter()
        
        try:
            # Execute the original function
            result = func(*args, **kwargs)
        except Exception as e:
            # If an exception occurs, still calculate and print execution time
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            print(f"Execution of {func.__name__} failed. Time taken: {execution_time:.4f} seconds")
            raise
        
        # Record end time
        end_time = time.perf_counter()
        
        # Calculate execution time
        execution_time = end_time - start_time
        
        # Print execution time
        print(f"Execution of {func.__name__} took {execution_time:.4f} seconds")
        
        return result
    
    return wrapper