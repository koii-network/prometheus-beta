from functools import wraps
import threading

class FunctionCallLogger:
    """
    A class to log the number of times functions are called.
    Thread-safe implementation to handle concurrent function calls.
    """
    def __init__(self):
        self._call_counts = {}
        self._lock = threading.Lock()

    def log_calls(self, func):
        """
        A decorator that logs the number of times a function is called.
        
        Args:
            func (callable): The function to be wrapped and logged.
        
        Returns:
            callable: The wrapped function that logs call counts.
        """
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Use thread-safe increment
            with self._lock:
                if func.__name__ not in self._call_counts:
                    self._call_counts[func.__name__] = 0
                self._call_counts[func.__name__] += 1
            
            # Call the original function
            return func(*args, **kwargs)
        
        return wrapper
    
    def get_call_count(self, func_name):
        """
        Get the number of times a specific function has been called.
        
        Args:
            func_name (str): Name of the function to check.
        
        Returns:
            int: Number of times the function has been called.
        """
        with self._lock:
            return self._call_counts.get(func_name, 0)
    
    def reset_call_count(self, func_name=None):
        """
        Reset call count for a specific function or all functions.
        
        Args:
            func_name (str, optional): Name of the function to reset. 
                                       If None, resets all function counts.
        """
        with self._lock:
            if func_name is None:
                self._call_counts.clear()
            elif func_name in self._call_counts:
                del self._call_counts[func_name]