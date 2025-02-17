from functools import wraps
from collections import defaultdict

class FunctionCallLogger:
    """
    A class to log and track the number of times functions are called.
    """
    _call_counts = defaultdict(int)

    @classmethod
    def log_calls(cls, func):
        """
        A decorator that logs the number of times a function is called.
        
        Args:
            func (callable): The function to be wrapped and tracked.
        
        Returns:
            callable: The wrapped function that tracks call counts.
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Increment the call count for this specific function
            cls._call_counts[func.__name__] += 1
            
            # Call the original function
            return func(*args, **kwargs)
        
        return wrapper
    
    @classmethod
    def get_call_count(cls, func_name):
        """
        Get the number of times a function has been called.
        
        Args:
            func_name (str): The name of the function to check.
        
        Returns:
            int: The number of times the function has been called.
        """
        return cls._call_counts.get(func_name, 0)
    
    @classmethod
    def reset_call_counts(cls):
        """
        Reset the call counts for all functions.
        """
        cls._call_counts.clear()