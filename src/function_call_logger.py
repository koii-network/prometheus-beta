from functools import wraps
from collections import defaultdict

def count_calls(func):
    """
    A decorator that logs the number of times a function is called.
    
    Args:
        func (callable): The function to be decorated.
    
    Returns:
        callable: A wrapped function that tracks call count.
    """
    # Use a defaultdict to track function call counts
    call_counts = defaultdict(int)
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Increment the call count for this specific function
        call_counts[func.__name__] += 1
        
        # Call the original function
        return func(*args, **kwargs)
    
    def get_call_count():
        """
        Returns the number of times the decorated function has been called.
        
        Returns:
            int: The number of times the function has been called.
        """
        return call_counts[func.__name__]
    
    # Attach the get_call_count method to the wrapper
    wrapper.get_call_count = get_call_count
    
    return wrapper