from functools import wraps
from typing import Callable, Any, Dict

class FunctionCallLogger:
    """
    A class to track and log function call counts.
    """
    _call_counts: Dict[str, int] = {}

    @classmethod
    def log_calls(cls, func: Callable) -> Callable:
        """
        A decorator to log the number of times a function is called.

        Args:
            func (Callable): The function to be decorated.

        Returns:
            Callable: The wrapped function that tracks call counts.
        """
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Increment the call count for this function
            func_name = func.__name__
            cls._call_counts[func_name] = cls._call_counts.get(func_name, 0) + 1
            
            # Call the original function
            return func(*args, **kwargs)
        
        return wrapper

    @classmethod
    def get_call_count(cls, func_name: str) -> int:
        """
        Get the number of times a function has been called.

        Args:
            func_name (str): The name of the function to check.

        Returns:
            int: The number of times the function has been called.
             Returns 0 if the function has never been called.
        """
        return cls._call_counts.get(func_name, 0)

    @classmethod
    def reset_call_counts(cls) -> None:
        """
        Reset the call counts for all functions.
        """
        cls._call_counts.clear()