import time
import functools
from typing import Callable, Any

def measure_execution_time(func: Callable[..., Any]) -> Callable[..., Any]:
    """
    A decorator that measures and returns the execution time of a function.

    Args:
        func (Callable): The function whose execution time is to be measured.

    Returns:
        Callable: A wrapped function that returns a tuple of (original_return_value, execution_time).

    Raises:
        TypeError: If the input is not a callable object.
    """
    # Validate input before decorating
    if not callable(func):
        raise TypeError("Input must be a callable object")

    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> tuple:
        """
        Wrapper function that measures execution time of the original function.

        Args:
            *args: Positional arguments to pass to the original function.
            **kwargs: Keyword arguments to pass to the original function.

        Returns:
            tuple: A tuple containing (original_return_value, execution_time_in_seconds)
        """
        # Measure start time
        start_time = time.perf_counter()

        # Execute the function
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            # If an exception occurs, still calculate execution time
            end_time = time.perf_counter()
            execution_time = end_time - start_time
            raise e

        # Measure end time and calculate execution time
        end_time = time.perf_counter()
        execution_time = end_time - start_time

        # Return original result and execution time
        return (result, execution_time)

    return wrapper