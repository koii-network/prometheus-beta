import pytest
from src.find_min_max import find_min_max

def test_find_min_max_positive_numbers():
    assert find_min_max([1, 2, 3, 4, 5]) == (1, 5)

def test_find_min_max_mixed_numbers():
    assert find_min_max([-10, 0, 10, 5, -5]) == (-10, 10)

def test_find_min_max_single_element():
    assert find_min_max([42]) == (42, 42)

def test_find_min_max_float_numbers():
    assert find_min_max([1.5, 2.3, -0.7, 10.1]) == (-0.7, 10.1)

def test_find_min_max_empty_list():
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_min_max([])

def test_find_min_max_invalid_input():
    with pytest.raises(TypeError, match="All elements in the list must be numbers"):
        find_min_max([1, 2, '3', 4, 5])