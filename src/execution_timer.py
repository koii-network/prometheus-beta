import time
from functools import wraps
from typing import Callable, Any

def measure_execution_time(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    A decorator that measures and returns the execution time of a function.

    Args:
        func (Callable): The function to measure execution time for.

    Returns:
        Callable: A wrapped function that returns a tuple of (original return value, execution time in seconds).

    Raises:
        TypeError: If the input is not a callable function.
    """
    # Check if input is callable before wrapping
    if not callable(func):
        raise TypeError("Input must be a callable function")

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> tuple[Any, float]:
        """
        Wrapper function that measures execution time.

        Args:
            *args: Positional arguments to pass to the original function.
            **kwargs: Keyword arguments to pass to the original function.

        Returns:
            tuple: A tuple containing the original function's return value and its execution time.
        """
        # Measure start time
        start_time = time.perf_counter()

        try:
            # Execute the function
            result = func(*args, **kwargs)
        except Exception as e:
            # Measure end time even if an exception occurs
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            # Re-raise the original exception
            raise

        # Measure end time
        end_time = time.perf_counter()
        
        # Calculate execution time
        execution_time = end_time - start_time

        # Return result and execution time
        return result, execution_time

    return wrapper