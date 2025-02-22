import pytest
from src.mid_range_indices import find_mid_range_indices

def test_odd_length_list():
    # Odd-length list with centered middle value
    lst = [1, 3, 5, 7, 9]
    assert find_mid_range_indices(lst, 2) == [1, 2, 3]

def test_even_length_list():
    # Even-length list (middle value would be 5)
    lst = [1, 3, 5, 7, 9, 11]
    assert find_mid_range_indices(lst, 2) == [1, 2, 3]

def test_exact_range():
    # Test with a tight range
    lst = [1, 3, 5, 7, 9]
    assert find_mid_range_indices(lst, 0) == [2]

def test_wide_range():
    # Test with a wide range
    lst = [1, 3, 5, 7, 9, 11, 13, 15]
    assert find_mid_range_indices(lst, 5) == [0, 1, 2, 3, 4, 5, 6]

def test_empty_list_raises_error():
    # Test that empty list raises ValueError
    with pytest.raises(ValueError):
        find_mid_range_indices([], 2)

def test_negative_numbers():
    # Test with a list containing negative numbers
    lst = [-9, -7, -5, -3, -1, 1, 3, 5, 7, 9]
    assert find_mid_range_indices(lst, 2) == [4, 5, 6]

def test_single_element_list():
    # Test with a single-element list
    lst = [5]
    assert find_mid_range_indices(lst, 2) == [0]