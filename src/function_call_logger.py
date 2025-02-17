from functools import wraps
from collections import defaultdict

def call_counter(func):
    """
    A decorator that logs and tracks the number of times a function is called.
    
    Args:
        func (callable): The function to be decorated
    
    Returns:
        callable: A wrapped function that tracks call counts
    """
    # Use a defaultdict to track call counts for different functions
    call_counts = defaultdict(int)
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Increment the call count for this specific function
        call_counts[func.__name__] += 1
        
        # Call the original function
        return func(*args, **kwargs)
    
    # Add a method to retrieve the current call count
    def get_call_count():
        return call_counts[func.__name__]
    
    # Add a method to reset the call count
    def reset_call_count():
        call_counts[func.__name__] = 0
    
    # Attach methods to the wrapper
    wrapper.get_call_count = get_call_count
    wrapper.reset_call_count = reset_call_count
    
    return wrapper