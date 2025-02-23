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

def test_radix_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    assert radix_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_radix_sort_with_zeros():
    """Test sorting a list that includes zeros."""
    assert radix_sort([0, 0, 0, 1, 2, 0]) == [0, 0, 0, 0, 1, 2]

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        radix_sort("not a list")

def test_invalid_element_type():
    """Test that ValueError is raised for negative or non-integer elements."""
    with pytest.raises(ValueError, match="All elements must be non-negative integers"):
        radix_sort([1, 2, -3, 4])
    
    with pytest.raises(ValueError, match="All elements must be non-negative integers"):
        radix_sort([1, 2, 3.14, 4])