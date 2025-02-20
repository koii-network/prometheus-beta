import pytest
from src.fibonacci_zigzag import fibonacci_zigzag

def test_fibonacci_zigzag_basic():
    """Test basic functionality with different input sizes."""
    assert fibonacci_zigzag(1) == [0]
    assert fibonacci_zigzag(2) == [0, 1]
    assert fibonacci_zigzag(3) == [0, 2, 1]
    assert fibonacci_zigzag(4) == [0, 2, 1, 3]
    assert fibonacci_zigzag(5) == [0, 2, 1, 3, 5]
    assert fibonacci_zigzag(6) == [0, 2, 1, 3, 5, 8]

def test_fibonacci_zigzag_larger_input():
    """Test with a larger input to verify zigzag pattern."""
    result = fibonacci_zigzag(10)
    expected = [0, 2, 1, 3, 5, 8, 13, 21, 34, 55]
    assert result == expected

def test_fibonacci_zigzag_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_zigzag(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_zigzag(-1)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_zigzag(1.5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_zigzag("3")
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_zigzag(None)