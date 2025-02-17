import time
import functools
from typing import Callable, Any

def measure_execution_time(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    A decorator that measures and prints the execution time of a function.
    
    Args:
        func (Callable): The function whose execution time is to be measured.
    
    Returns:
        Callable: A wrapped function that prints execution time before returning result.
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Record start time
        start_time = time.perf_counter()
        
        try:
            # Execute the function
            result = func(*args, **kwargs)
            
            # Calculate execution time
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            
            # Print execution time
            print(f"Function '{func.__name__}' took {execution_time:.6f} seconds to execute.")
            
            return result
        
        except Exception as e:
            # Measure time even if an exception occurs
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            
            print(f"Function '{func.__name__}' raised an exception after {execution_time:.6f} seconds.")
            raise
    
    return wrapper