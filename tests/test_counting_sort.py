import pytest
from src.counting_sort import counting_sort

def test_counting_sort_basic():
    """Test basic sorting of positive integers"""
    arr = [4, 2, 2, 8, 3, 3, 1]
    assert counting_sort(arr) == [1, 2, 2, 3, 3, 4, 8]

def test_counting_sort_empty_list():
    """Test sorting an empty list"""
    assert counting_sort([]) == []

def test_counting_sort_single_element():
    """Test sorting a list with a single element"""
    assert counting_sort([5]) == [5]

def test_counting_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    arr = [1, 2, 3, 4, 5]
    assert counting_sort(arr) == [1, 2, 3, 4, 5]

def test_counting_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    arr = [5, 4, 3, 2, 1]
    assert counting_sort(arr) == [1, 2, 3, 4, 5]

def test_counting_sort_with_duplicates():
    """Test sorting a list with many duplicates"""
    arr = [3, 3, 3, 3, 3]
    assert counting_sort(arr) == [3, 3, 3, 3, 3]

def test_counting_sort_invalid_input_type():
    """Test handling of non-list input"""
    with pytest.raises(TypeError):
        counting_sort(123)

def test_counting_sort_invalid_element_type():
    """Test handling of non-integer elements"""
    with pytest.raises(TypeError):
        counting_sort([1, 2, 'a', 4])

def test_counting_sort_negative_numbers():
    """Test handling of negative numbers"""
    with pytest.raises(ValueError):
        counting_sort([1, 2, -3, 4])