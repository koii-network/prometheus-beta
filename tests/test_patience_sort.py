import pytest
from src.patience_sort import patience_sort

def test_empty_list():
    """Test sorting an empty list."""
    assert patience_sort([]) == []

def test_single_element_list():
    """Test sorting a list with a single element."""
    assert patience_sort([5]) == [5]

def test_already_sorted_list():
    """Test sorting a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    assert patience_sort(input_list) == input_list

def test_reverse_sorted_list():
    """Test sorting a list in reverse order."""
    input_list = [5, 4, 3, 2, 1]
    assert patience_sort(input_list) == [1, 2, 3, 4, 5]

def test_unsorted_list():
    """Test sorting a randomly unsorted list."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert patience_sort(input_list) == sorted(input_list)

def test_list_with_duplicates():
    """Test sorting a list with duplicate elements."""
    input_list = [3, 3, 3, 1, 1, 4, 4]
    assert patience_sort(input_list) == sorted(input_list)

def test_list_with_negative_numbers():
    """Test sorting a list with negative numbers."""
    input_list = [-3, 0, -1, 5, -2, 4]
    assert patience_sort(input_list) == sorted(input_list)

def test_list_with_mixed_types():
    """Test sorting a list of strings."""
    input_list = ['banana', 'apple', 'cherry', 'date']
    assert patience_sort(input_list) == sorted(input_list)

def test_invalid_input_type():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        patience_sort("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        patience_sort(123)
    with pytest.raises(TypeError, match="Input must be a list"):
        patience_sort(None)