import pytest
from src.fibonacci_zigzag import fibonacci_zigzag

def test_fibonacci_zigzag_basic():
    """Test basic functionality of fibonacci_zigzag"""
    assert fibonacci_zigzag(1) == [0]
    assert fibonacci_zigzag(2) == [0, 1]
    assert fibonacci_zigzag(3) == [0, 2, 1]
    assert fibonacci_zigzag(4) == [0, 2, 3, 1]
    assert fibonacci_zigzag(5) == [0, 2, 3, 5, 1]

def test_fibonacci_zigzag_larger_n():
    """Test fibonacci_zigzag with larger input values"""
    result_6 = fibonacci_zigzag(6)
    assert result_6 == [0, 2, 3, 5, 8, 1]
    
    result_7 = fibonacci_zigzag(7)
    assert result_7 == [0, 2, 3, 5, 8, 13, 1]

def test_fibonacci_zigzag_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_zigzag(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_zigzag(-1)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_zigzag(1.5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_zigzag("3")