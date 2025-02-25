import pytest
from src.counting_sort import counting_sort

def test_normal_case():
    """Test sorting a list of non-negative integers."""
    assert counting_sort([4, 2, 2, 8, 3, 3, 1]) == [1, 2, 2, 3, 3, 4, 8]

def test_empty_list():
    """Test sorting an empty list."""
    assert counting_sort([]) == []

def test_single_element():
    """Test sorting a list with a single element."""
    assert counting_sort([5]) == [5]

def test_already_sorted():
    """Test sorting an already sorted list."""
    assert counting_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_reverse_sorted():
    """Test sorting a reverse sorted list."""
    assert counting_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_with_zeros():
    """Test sorting a list containing zeros."""
    assert counting_sort([0, 0, 1, 2, 0]) == [0, 0, 0, 1, 2]

def test_raises_type_error_for_non_list():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        counting_sort("not a list")

def test_raises_type_error_for_non_integers():
    """Test that a TypeError is raised for non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        counting_sort([1, 2, 'a', 3])

def test_raises_value_error_for_negative_numbers():
    """Test that a ValueError is raised for negative numbers."""
    with pytest.raises(ValueError, match="Counting sort only works with non-negative integers"):
        counting_sort([1, 2, -3, 4])