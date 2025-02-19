import pytest
from src.fibonacci import fibonacci

def test_fibonacci_first_second_numbers():
    """Test the first two Fibonacci numbers."""
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1

def test_fibonacci_subsequent_numbers():
    """Test subsequent Fibonacci numbers."""
    assert fibonacci(3) == 2  # 1 + 1
    assert fibonacci(4) == 3  # 1 + 2
    assert fibonacci(5) == 5  # 2 + 3
    assert fibonacci(6) == 8  # 3 + 5

def test_fibonacci_invalid_input():
    """Test invalid input raises ValueError."""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci(0)
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci(-1)
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci(-100)