import pytest
from src.two_sum_check import two_sum_target

def test_two_sum_target_basic_positive():
    """Test basic positive scenario where two numbers sum to target."""
    assert two_sum_target([1, 2, 3, 4, 5], 7) == True
    assert two_sum_target([10, 15, 3, 7], 17) == True

def test_two_sum_target_basic_negative():
    """Test scenarios where no two numbers sum to target."""
    assert two_sum_target([1, 2, 3, 4, 5], 20) == False
    assert two_sum_target([10, 15, 3, 7], 100) == False

def test_two_sum_target_edge_cases():
    """Test edge cases like empty list, single element, or zero."""
    assert two_sum_target([], 5) == False
    assert two_sum_target([5], 10) == False
    assert two_sum_target([0, 0], 0) == False

def test_two_sum_target_type_errors():
    """Test type error handling."""
    with pytest.raises(TypeError, match="Input must be a list"):
        two_sum_target(123, 10)
    
    with pytest.raises(TypeError, match="All elements must be integers"):
        two_sum_target([1, 2, '3'], 6)
    
    with pytest.raises(TypeError, match="All elements must be integers"):
        two_sum_target([1, 2, 3.5], 6)

def test_two_sum_target_duplicate_error():
    """Test handling of duplicate values in input."""
    with pytest.raises(ValueError, match="Input list must contain unique integers"):
        two_sum_target([1, 2, 2, 3], 4)

def test_two_sum_target_zero_and_negative():
    """Test scenarios with zero and negative numbers."""
    assert two_sum_target([-1, 0, 1, 2], 1) == True
    assert two_sum_target([-5, -4, -3, -2, -1], -8) == True
    assert two_sum_target([-5, -4, -3, -2, -1], 100) == False