import pytest
from src.is_sorted import is_sorted

def test_empty_list():
    """Test that an empty list is considered sorted."""
    assert is_sorted([]) == True

def test_single_element_list():
    """Test that a single-element list is considered sorted."""
    assert is_sorted([42]) == True

def test_ascending_sorted_list():
    """Test a list sorted in ascending order."""
    assert is_sorted([1, 2, 3, 4, 5]) == True

def test_descending_sorted_list():
    """Test a list sorted in descending order."""
    assert is_sorted([5, 4, 3, 2, 1], ascending=False) == True

def test_unsorted_list_ascending():
    """Test an unsorted list fails ascending check."""
    assert is_sorted([1, 3, 2, 4, 5]) == False

def test_unsorted_list_descending():
    """Test an unsorted list fails descending check."""
    assert is_sorted([5, 3, 4, 2, 1], ascending=False) == False

def test_list_with_duplicates_ascending():
    """Test ascending list with duplicate elements."""
    assert is_sorted([1, 2, 2, 3, 3, 4]) == True

def test_list_with_duplicates_descending():
    """Test descending list with duplicate elements."""
    assert is_sorted([4, 3, 3, 2, 2, 1], ascending=False) == True

def test_float_list():
    """Test sorting with floating point numbers."""
    assert is_sorted([1.1, 2.2, 3.3, 4.4]) == True

def test_mixed_numeric_types():
    """Test sorting with mixed numeric types."""
    assert is_sorted([1, 2.0, 3, 4.5]) == True