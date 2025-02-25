from functools import wraps
from collections import defaultdict

class FunctionCallTracker:
    """
    A decorator class to track the number of times a function is called.
    """
    _call_counts = defaultdict(int)

    @classmethod
    def track(cls, func):
        """
        Decorator to track the number of times a function is called.
        
        Args:
            func (callable): The function to be tracked.
        
        Returns:
            callable: The wrapped function with call tracking.
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            cls._call_counts[func.__name__] += 1
            return func(*args, **kwargs)
        return wrapper

    @classmethod
    def get_call_count(cls, func_name):
        """
        Get the number of times a function has been called.
        
        Args:
            func_name (str): The name of the function.
        
        Returns:
            int: The number of times the function has been called.
        """
        return cls._call_counts[func_name]

    @classmethod
    def reset_call_counts(cls):
        """
        Reset the call counts for all tracked functions.
        """
        cls._call_counts.clear()