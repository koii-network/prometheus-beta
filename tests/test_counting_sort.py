import pytest
from src.counting_sort import counting_sort

def test_counting_sort_basic():
    """Test basic sorting functionality"""
    arr = [4, 2, 2, 8, 3, 3, 1]
    assert counting_sort(arr) == [1, 2, 2, 3, 3, 4, 8]

def test_counting_sort_empty_list():
    """Test sorting an empty list"""
    assert counting_sort([]) == []

def test_counting_sort_single_element():
    """Test sorting a list with a single element"""
    assert counting_sort([5]) == [5]

def test_counting_sort_already_sorted():
    """Test sorting an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert counting_sort(arr) == [1, 2, 3, 4, 5]

def test_counting_sort_duplicate_elements():
    """Test sorting a list with multiple duplicate elements"""
    arr = [5, 5, 5, 3, 3, 1, 1, 1]
    assert counting_sort(arr) == [1, 1, 1, 3, 3, 5, 5, 5]

def test_counting_sort_invalid_input_type():
    """Test handling of invalid input type"""
    with pytest.raises(TypeError):
        counting_sort("not a list")

def test_counting_sort_negative_elements():
    """Test handling of negative elements"""
    with pytest.raises(ValueError):
        counting_sort([1, 2, -3, 4])

def test_counting_sort_non_integer():
    """Test handling of non-integer elements"""
    with pytest.raises(ValueError):
        counting_sort([1, 2, 3.5, 4])