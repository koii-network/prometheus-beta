import pytest
from src.two_sum import find_two_sum_indices

def test_find_two_sum_indices_basic():
    assert find_two_sum_indices([2, 7, 11, 15], 9) == [0, 1]

def test_find_two_sum_indices_multiple_solutions():
    # First solution in the list should be returned
    assert find_two_sum_indices([3, 2, 4], 6) == [1, 2]

def test_find_two_sum_indices_no_solution():
    assert find_two_sum_indices([1, 2, 3, 4], 10) == []

def test_find_two_sum_indices_negative_numbers():
    assert find_two_sum_indices([-1, -2, -3, -4], -7) == [2, 3]

def test_find_two_sum_indices_zero_sum():
    assert find_two_sum_indices([0, 0], 0) == [0, 1]

def test_find_two_sum_invalid_input_type():
    with pytest.raises(TypeError, match="Input must be a list"):
        find_two_sum_indices("not a list", 5)

def test_find_two_sum_invalid_target_type():
    with pytest.raises(TypeError, match="Target must be an integer"):
        find_two_sum_indices([1, 2, 3], "not an int")

def test_find_two_sum_empty_list():
    assert find_two_sum_indices([], 5) == []