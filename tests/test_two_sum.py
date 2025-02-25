import pytest
from src.two_sum import two_sum

def test_two_sum_basic_case():
    """Test a basic scenario where solution exists"""
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_two_sum_no_solution():
    """Test when no solution exists"""
    assert two_sum([1, 2, 3, 4], 10) == []

def test_two_sum_multiple_solutions():
    """Test case where multiple solutions might exist"""
    result = two_sum([3, 2, 4], 6)
    assert result == [1, 2]

def test_two_sum_negative_numbers():
    """Test with negative numbers"""
    assert two_sum([-1, -2, -3, -4], -5) == [1, 2]

def test_two_sum_zero_sum():
    """Test with zero target sum"""
    assert two_sum([0, 0], 0) == [0, 1]

def test_two_sum_invalid_input_none():
    """Test handling of None input"""
    with pytest.raises(ValueError):
        two_sum(None, 5)
    with pytest.raises(ValueError):
        two_sum([1, 2, 3], None)

def test_two_sum_invalid_input_type():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        two_sum("not a list", 5)
    with pytest.raises(TypeError):
        two_sum([1, 2, 3], "not an int")

def test_two_sum_empty_list():
    """Test with an empty list"""
    assert two_sum([], 5) == []