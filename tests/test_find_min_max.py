import pytest
from src.find_min_max import find_min_max

def test_find_min_max_normal_case():
    assert find_min_max([1, 2, 3, 4, 5]) == (1, 5)
    assert find_min_max([-10, 0, 10]) == (-10, 10)

def test_find_min_max_single_element():
    assert find_min_max([42]) == (42, 42)

def test_find_min_max_float_numbers():
    assert find_min_max([1.5, 2.7, -3.2, 0]) == (-3.2, 2.7)

def test_find_min_max_empty_list():
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_min_max([])

def test_find_min_max_non_numeric():
    with pytest.raises(TypeError, match="All elements in the list must be numeric"):
        find_min_max([1, 2, "three"])
        find_min_max([1, 2, None])