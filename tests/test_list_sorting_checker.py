import pytest
from src.list_sorting_checker import is_sorted

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
    """Test an unsorted list with default ascending check."""
    assert is_sorted([1, 3, 2, 4, 5]) == False

def test_unsorted_list_descending():
    """Test an unsorted list with descending check."""
    assert is_sorted([5, 3, 4, 2, 1], ascending=False) == False

def test_list_with_duplicates_ascending():
    """Test a sorted list with duplicate values in ascending order."""
    assert is_sorted([1, 2, 2, 3, 3, 4]) == True

def test_list_with_duplicates_descending():
    """Test a sorted list with duplicate values in descending order."""
    assert is_sorted([4, 3, 3, 2, 2, 1], ascending=False) == True

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError):
        is_sorted("not a list")

def test_mixed_type_list():
    """Test a list with elements of different but comparable types."""
    assert is_sorted([1, 2.5, 3]) == True
    assert is_sorted([5, 4.5, 3]) == False