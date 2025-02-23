import time
import pytest
from src.execution_timer import measure_execution_time


def test_measure_execution_time(capsys):
    """
    Test that the decorator correctly measures and prints execution time.
    """
    @measure_execution_time
    def slow_function():
        time.sleep(0.1)
        return 42

    # Call the function and check the result
    result = slow_function()
    assert result == 42

    # Capture the printed output
    captured = capsys.readouterr()
    
    # Check that execution time was printed
    assert "Execution of slow_function took" in captured.out
    assert "seconds" in captured.out


def test_measure_execution_time_with_args(capsys):
    """
    Test the decorator with a function that takes arguments.
    """
    @measure_execution_time
    def add_numbers(a, b):
        time.sleep(0.05)
        return a + b

    # Call the function and check the result
    result = add_numbers(3, 5)
    assert result == 8

    # Capture the printed output
    captured = capsys.readouterr()
    
    # Check that execution time was printed
    assert "Execution of add_numbers took" in captured.out
    assert "seconds" in captured.out


def test_measure_execution_time_with_exception(capsys):
    """
    Test that the decorator handles exceptions while still measuring time.
    """
    @measure_execution_time
    def function_with_error():
        time.sleep(0.05)
        raise ValueError("Test error")

    # Expect the function to raise the original exception
    with pytest.raises(ValueError, match="Test error"):
        function_with_error()

    # Capture the printed output
    captured = capsys.readouterr()
    
    # Check that execution time was printed before the exception
    assert "Execution of function_with_error failed. Time taken:" in captured.out
    assert "seconds" in captured.out


def test_decorator_preserves_function_metadata():
    """
    Test that the decorator preserves the original function's metadata.
    """
    @measure_execution_time
    def example_function(x, y):
        """Docstring for example function."""
        return x + y

    assert example_function.__name__ == "example_function"
    assert "Docstring for example function." in example_function.__doc__