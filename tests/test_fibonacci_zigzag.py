import pytest
from src.fibonacci_zigzag import fibonacci_zigzag

def test_fibonacci_zigzag_basic():
    """Test basic functionality of fibonacci_zigzag."""
    assert fibonacci_zigzag(1) == [0]
    assert fibonacci_zigzag(2) == [0, 1]
    assert fibonacci_zigzag(5) == [0, 1, 1, 2, 3]
    assert fibonacci_zigzag(7) == [0, 1, 1, 2, 3, 5, 8]

def test_fibonacci_zigzag_larger_input():
    """Test fibonacci_zigzag with larger inputs."""
    result = fibonacci_zigzag(10)
    assert len(result) == 10
    assert result == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def test_fibonacci_zigzag_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_zigzag(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_zigzag(-1)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_zigzag(1.5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_zigzag("5")

def test_fibonacci_zigzag_type_check():
    """Ensure only integer inputs are accepted."""
    with pytest.raises(ValueError):
        fibonacci_zigzag(None)
    
    with pytest.raises(ValueError):
        fibonacci_zigzag([1, 2, 3])
    
    with pytest.raises(ValueError):
        fibonacci_zigzag({})