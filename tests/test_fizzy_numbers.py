import pytest
from src.fizzy_numbers import find_fizzy_numbers

def test_fizzy_numbers_basic():
    """Test basic functionality of find_fizzy_numbers."""
    assert find_fizzy_numbers(10) == [3, 6, 7, 9]

def test_fizzy_numbers_larger_range():
    """Test find_fizzy_numbers with a larger range."""
    expected = [3, 6, 7, 9, 12, 14, 15, 18]
    assert find_fizzy_numbers(20) == expected

def test_fizzy_numbers_edge_cases():
    """Test edge cases and boundary conditions."""
    # Single digit cases
    assert find_fizzy_numbers(1) == []
    assert find_fizzy_numbers(3) == [3]
    assert find_fizzy_numbers(7) == [3, 6, 7]

def test_invalid_inputs():
    """Test error handling for invalid inputs."""
    # Test non-positive integers
    with pytest.raises(ValueError):
        find_fizzy_numbers(0)
    
    with pytest.raises(ValueError):
        find_fizzy_numbers(-5)
    
    # Test non-integer inputs
    with pytest.raises(ValueError):
        find_fizzy_numbers(3.14)
    
    with pytest.raises(ValueError):
        find_fizzy_numbers("10")
    
    with pytest.raises(ValueError):
        find_fizzy_numbers(None)