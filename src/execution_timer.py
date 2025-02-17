import time
import functools

def measure_execution_time(func):
    """
    A decorator that measures and prints the execution time of a function.
    
    Args:
        func (callable): The function to be timed.
    
    Returns:
        callable: A wrapper function that times the original function's execution.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Record the start time
        start_time = time.perf_counter()
        
        try:
            # Execute the original function
            result = func(*args, **kwargs)
            
            # Calculate and print the execution time
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            print(f"Function '{func.__name__}' took {execution_time:.4f} seconds to execute.")
            
            return result
        
        except Exception as e:
            # If an exception occurs, still print the execution time
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            print(f"Function '{func.__name__}' raised an exception after {execution_time:.4f} seconds.")
            raise
    
    return wrapper