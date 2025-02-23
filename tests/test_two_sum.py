import pytest
from src.two_sum import two_sum

def test_basic_two_sum():
    """Test finding two indices that sum to the target"""
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_no_solution():
    """Test when no solution exists"""
    assert two_sum([2, 3, 4], 10) == []

def test_multiple_solutions():
    """Verify the function returns the first valid solution"""
    assert two_sum([3, 2, 4], 6) == [1, 2]

def test_duplicate_numbers():
    """Test with duplicate numbers in the array"""
    assert two_sum([3, 3], 6) == [0, 1]

def test_empty_list():
    """Test with an empty list"""
    assert two_sum([], 5) == []

def test_invalid_input_not_list():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        two_sum("not a list", 5)

def test_invalid_elements():
    """Test raising TypeError for non-numeric elements"""
    with pytest.raises(TypeError, match="All list elements must be numbers"):
        two_sum([1, '2', 3], 5)

def test_invalid_target():
    """Test raising ValueError for invalid target"""
    with pytest.raises(ValueError, match="Target must be a number"):
        two_sum([1, 2, 3], "not a number")

def test_negative_numbers():
    """Test with negative numbers"""
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4]

def test_floating_point_numbers():
    """Test with floating point numbers"""
    assert two_sum([1.5, 2.5, 3.0, 4.0], 5.5) == [0, 1]