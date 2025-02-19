import pytest
from src.two_sum import find_two_sum_indices

def test_basic_two_sum():
    """Test basic scenario with a solution"""
    numbers = [2, 7, 11, 15]
    target_sum = 9
    result = find_two_sum_indices(numbers, target_sum)
    assert sorted(result) == [0, 1]

def test_multiple_solutions():
    """Test with first valid solution"""
    numbers = [3, 2, 4, 1, 5]
    target_sum = 6
    result = find_two_sum_indices(numbers, target_sum)
    assert result in [[1, 2]]  # Update to match expected first solution

def test_no_solution():
    """Test when no indices add up to target sum"""
    numbers = [1, 2, 3, 4]
    target_sum = 10
    result = find_two_sum_indices(numbers, target_sum)
    assert result == []

def test_duplicate_numbers():
    """Test with duplicate numbers"""
    numbers = [3, 3]
    target_sum = 6
    result = find_two_sum_indices(numbers, target_sum)
    assert result == [0, 1]

def test_negative_numbers():
    """Test with negative numbers"""
    numbers = [-1, -2, -3, -4, -5]
    target_sum = -8
    result = find_two_sum_indices(numbers, target_sum)
    assert sorted(result) == [2, 4]

def test_empty_list():
    """Test with an empty list"""
    numbers = []
    target_sum = 5
    result = find_two_sum_indices(numbers, target_sum)
    assert result == []

def test_invalid_input_type():
    """Test with invalid input type for numbers"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_two_sum_indices("not a list", 5)

def test_invalid_target_sum_type():
    """Test with invalid type for target sum"""
    with pytest.raises(TypeError, match="Target sum must be an integer"):
        find_two_sum_indices([1, 2, 3], "not an int")

def test_non_numeric_list():
    """Test with non-numeric list elements"""
    with pytest.raises(ValueError, match="List must contain only numeric elements"):
        find_two_sum_indices([1, 2, "3"], 5)