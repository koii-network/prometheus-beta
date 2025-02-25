import pytest
from src.middle_range_indices import find_middle_range_indices

def test_odd_length_list_default_range():
    """Test middle range indices for an odd-length list with default range."""
    test_list = [1, 2, 3, 4, 5]
    assert find_middle_range_indices(test_list) == [2]

def test_even_length_list_default_range():
    """Test middle range indices for an even-length list with default range."""
    test_list = [1, 2, 3, 4, 5, 6]
    assert find_middle_range_indices(test_list) == [2, 3]

def test_custom_range_size():
    """Test middle range indices with a custom range size."""
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert find_middle_range_indices(test_list, range_size=2) == [3, 4, 5]

def test_range_size_zero():
    """Test middle range indices with range size of zero."""
    test_list = [1, 2, 3, 4, 5]
    assert find_middle_range_indices(test_list, range_size=0) == [2]

def test_large_range_size():
    """Test middle range indices with range size larger than list length."""
    test_list = [1, 2, 3, 4, 5]
    assert find_middle_range_indices(test_list, range_size=10) == list(range(5))

def test_empty_list():
    """Test middle range indices for an empty list."""
    assert find_middle_range_indices([]) == []

def test_single_element_list():
    """Test middle range indices for a single-element list."""
    assert find_middle_range_indices([42]) == [0]

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_middle_range_indices("not a list")

def test_invalid_range_size_type():
    """Test that TypeError is raised for non-integer range size."""
    with pytest.raises(TypeError, match="Range size must be an integer"):
        find_middle_range_indices([1, 2, 3], range_size="1")

def test_negative_range_size():
    """Test that ValueError is raised for negative range size."""
    with pytest.raises(ValueError, match="Range size cannot be negative"):
        find_middle_range_indices([1, 2, 3], range_size=-1)