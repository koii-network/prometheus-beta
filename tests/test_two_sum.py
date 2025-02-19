import pytest
from src.two_sum import two_sum

def test_two_sum_basic_positive():
    """Test that a valid two-sum combination is found"""
    assert two_sum([1, 2, 3, 4], 7) == True
    assert two_sum([10, 15, 3, 7], 17) == True

def test_two_sum_basic_negative():
    """Test that no two-sum combination is found"""
    assert two_sum([1, 2, 3, 4], 10) == False
    assert two_sum([5, 6, 7, 8], 20) == False

def test_two_sum_edge_cases():
    """Test edge cases like empty list and single element list"""
    assert two_sum([], 5) == False
    assert two_sum([1], 1) == False

def test_two_sum_type_errors():
    """Test type checking"""
    with pytest.raises(TypeError, match="Input must be a list"):
        two_sum(123, 10)
    
    with pytest.raises(TypeError, match="All elements must be integers"):
        two_sum([1, 2, '3'], 5)

def test_two_sum_duplicate_check():
    """Test duplicate input validation"""
    with pytest.raises(ValueError, match="Input list must contain unique integers"):
        two_sum([1, 2, 2, 3], 4)

def test_two_sum_zero_target():
    """Test scenarios with zero as the target"""
    assert two_sum([3, -3, 1, 2], 0) == True
    assert two_sum([1, 2, 3], 0) == False