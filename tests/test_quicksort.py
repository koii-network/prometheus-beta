import pytest
from src.quicksort import quicksort

def test_quicksort_normal_list():
    """Test sorting a normal list of integers"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list)
    assert quicksort(input_list) == expected

def test_quicksort_empty_list():
    """Test sorting an empty list"""
    assert quicksort([]) == []

def test_quicksort_single_element():
    """Test sorting a list with a single element"""
    assert quicksort([5]) == [5]

def test_quicksort_already_sorted():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert quicksort(input_list) == input_list

def test_quicksort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert quicksort(input_list) == expected

def test_quicksort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(input_list)
    assert quicksort(input_list) == expected

def test_quicksort_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-5, 2, -10, 0, 3, -7]
    expected = sorted(input_list)
    assert quicksort(input_list) == expected

def test_quicksort_invalid_input():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        quicksort("not a list")
    with pytest.raises(TypeError):
        quicksort(123)
    with pytest.raises(TypeError):
        quicksort(None)