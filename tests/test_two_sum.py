import pytest
from src.two_sum import find_two_sum

def test_basic_two_sum():
    """Test finding two indices that sum to target"""
    assert find_two_sum([2, 7, 11, 15], 9) == (0, 1)

def test_multiple_solutions():
    """Test that the first solution is returned"""
    assert find_two_sum([3, 2, 4], 6) == (1, 2)

def test_same_element_solution():
    """Test when the same element can be used twice"""
    result = find_two_sum([3, 3], 6)
    assert result == (0, 1) or result == (1, 0)

def test_no_solution():
    """Test when no solution exists"""
    assert find_two_sum([1, 2, 3, 4], 10) is None

def test_invalid_input_type():
    """Test handling of invalid input type"""
    with pytest.raises(TypeError):
        find_two_sum("not a list", 10)

def test_invalid_target_type():
    """Test handling of invalid target type"""
    with pytest.raises(TypeError):
        find_two_sum([1, 2, 3], "not an int")

def test_insufficient_list_length():
    """Test handling of list with less than 2 elements"""
    with pytest.raises(ValueError):
        find_two_sum([1], 2)

def test_large_list():
    """Test with a larger list"""
    large_list = list(range(1000))
    result = find_two_sum(large_list, 1999)
    assert result is not None
    a, b = result
    assert large_list[a] + large_list[b] == 1999

def test_negative_numbers():
    """Test with negative numbers"""
    assert find_two_sum([-1, -2, -3, -4, -5], -8) == (2, 4)