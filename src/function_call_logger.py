from functools import wraps
from typing import Callable, Any, Dict

class FunctionCallTracker:
    """
    A class to track the number of times functions are called.
    
    Attributes:
        _call_counts (Dict[str, int]): A dictionary storing call counts for functions.
    """
    _call_counts: Dict[str, int] = {}

    @classmethod
    def get_call_count(cls, func_name: str) -> int:
        """
        Retrieve the number of times a specific function has been called.
        
        Args:
            func_name (str): The name of the function to check.
        
        Returns:
            int: The number of times the function has been called.
        """
        return cls._call_counts.get(func_name, 0)

    @classmethod
    def log_function_call(cls, func_name: str) -> None:
        """
        Increment the call count for a specific function.
        
        Args:
            func_name (str): The name of the function being called.
        """
        cls._call_counts[func_name] = cls._call_counts.get(func_name, 0) + 1

    @classmethod
    def reset_call_counts(cls) -> None:
        """
        Reset the call counts for all functions.
        """
        cls._call_counts.clear()

def track_calls(func: Callable) -> Callable:
    """
    A decorator to track the number of times a function is called.
    
    Args:
        func (Callable): The function to track.
    
    Returns:
        Callable: The wrapped function with call tracking.
    """
    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Log the function call
        FunctionCallTracker.log_function_call(func.__name__)
        
        # Call the original function
        return func(*args, **kwargs)
    
    return wrapper