import pytest
from src.middle_range_indices import find_middle_range_indices

def test_odd_length_list_zero_range():
    """Test an odd-length list with zero range width"""
    sorted_list = [1, 2, 3, 4, 5]
    assert find_middle_range_indices(sorted_list, 0) == [2]

def test_even_length_list_zero_range():
    """Test an even-length list with zero range width"""
    sorted_list = [1, 2, 3, 4, 5, 6]
    assert find_middle_range_indices(sorted_list, 0) == [2]

def test_odd_length_list_positive_range():
    """Test an odd-length list with a positive range width"""
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = find_middle_range_indices(sorted_list, 2)
    assert set(result) == {3, 4, 5}

def test_even_length_list_positive_range():
    """Test an even-length list with a positive range width"""
    sorted_list = [1, 2, 3, 4, 5, 6, 7, 8]
    result = find_middle_range_indices(sorted_list, 1)
    assert set(result) == {3, 4}

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Cannot find middle range in an empty list"):
        find_middle_range_indices([], 1)

def test_negative_range_width_raises_error():
    """Test that a negative range width raises a ValueError"""
    with pytest.raises(ValueError, match="Range width must be non-negative"):
        find_middle_range_indices([1, 2, 3], -1)

def test_large_range_width():
    """Test a range width larger than the list"""
    sorted_list = [1, 2, 3, 4, 5]
    result = find_middle_range_indices(sorted_list, 100)
    assert result == list(range(len(sorted_list)))