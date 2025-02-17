import time
import functools

def measure_execution_time(func):
    """
    A decorator that measures and prints the execution time of a function.
    
    Args:
        func (callable): The function to be timed.
    
    Returns:
        callable: A wrapped function that prints its execution time.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Record the start time
        start_time = time.time()
        
        try:
            # Execute the original function
            result = func(*args, **kwargs)
            
            # Calculate and print execution time
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"Function '{func.__name__}' took {execution_time:.4f} seconds to execute.")
            
            return result
        
        except Exception as e:
            # If an exception occurs, still print the execution time
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"Function '{func.__name__}' threw an exception after {execution_time:.4f} seconds.")
            raise
    
    return wrapper