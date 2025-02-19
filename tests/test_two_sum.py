import pytest
from src.two_sum import find_two_sum_indices

def test_find_two_sum_indices_basic():
    """Test basic scenario with a valid two sum solution"""
    nums = [2, 7, 11, 15]
    target = 9
    result = find_two_sum_indices(nums, target)
    assert result == [0, 1]

def test_find_two_sum_indices_no_solution():
    """Test scenario where no solution exists"""
    nums = [2, 3, 4, 5]
    target = 10
    result = find_two_sum_indices(nums, target)
    assert result == []

def test_find_two_sum_indices_multiple_solutions():
    """Test that the function returns the first valid solution"""
    nums = [3, 2, 4, 2]
    target = 6
    result = find_two_sum_indices(nums, target)
    assert result == [1, 2]

def test_find_two_sum_indices_same_number():
    """Test case where the same number is used twice"""
    nums = [3, 3]
    target = 6
    result = find_two_sum_indices(nums, target)
    assert result == [0, 1]

def test_find_two_sum_indices_invalid_input_list():
    """Test that a TypeError is raised for invalid input list"""
    with pytest.raises(TypeError):
        find_two_sum_indices("not a list", 10)

def test_find_two_sum_indices_invalid_input_target():
    """Test that a TypeError is raised for invalid input target"""
    with pytest.raises(TypeError):
        find_two_sum_indices([1, 2, 3], "not a number")

def test_find_two_sum_indices_empty_list():
    """Test behavior with an empty list"""
    nums = []
    target = 10
    result = find_two_sum_indices(nums, target)
    assert result == []