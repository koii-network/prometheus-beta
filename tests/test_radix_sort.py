import pytest
from src.radix_sort import radix_sort

def test_radix_sort_basic():
    """Test basic sorting of a list of non-negative integers."""
    assert radix_sort([170, 45, 75, 90, 802, 24, 2, 66]) == [2, 24, 45, 66, 75, 90, 170, 802]

def test_radix_sort_empty_list():
    """Test sorting an empty list."""
    assert radix_sort([]) == []

def test_radix_sort_single_element():
    """Test sorting a list with a single element."""
    assert radix_sort([42]) == [42]

def test_radix_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    assert radix_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_radix_sort_with_zeros():
    """Test sorting a list with multiple zeros."""
    assert radix_sort([0, 0, 0, 1, 2, 0]) == [0, 0, 0, 0, 1, 2]

def test_radix_sort_invalid_input_type():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        radix_sort("not a list")

def test_radix_sort_negative_numbers():
    """Test that a ValueError is raised for negative numbers."""
    with pytest.raises(ValueError, match="All elements must be non-negative integers"):
        radix_sort([-1, 2, 3])

def test_radix_sort_non_integer_elements():
    """Test that a ValueError is raised for non-integer elements."""
    with pytest.raises(ValueError, match="All elements must be non-negative integers"):
        radix_sort([1, 2.5, 3])