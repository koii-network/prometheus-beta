import pytest
from src.fibonacci_zigzag import fibonacci_zigzag

def test_fibonacci_zigzag_basic_cases():
    assert fibonacci_zigzag(1) == [0]
    assert fibonacci_zigzag(2) == [0, 1]
    assert fibonacci_zigzag(3) == [0, 2, 1]
    assert fibonacci_zigzag(4) == [0, 2, 3, 1]
    assert fibonacci_zigzag(5) == [0, 2, 3, 5, 1]

def test_fibonacci_zigzag_larger_n():
    result = fibonacci_zigzag(7)
    expected = [0, 2, 3, 5, 8, 13, 1]
    assert result == expected

def test_fibonacci_zigzag_invalid_input():
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_zigzag(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_zigzag(-1)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_zigzag(3.5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_zigzag("not a number")