import pytest
from src.counting_sort import counting_sort

def test_basic_sorting():
    """Test basic sorting functionality"""
    arr = [4, 2, 2, 8, 3, 3, 1]
    assert counting_sort(arr) == [1, 2, 2, 3, 3, 4, 8]

def test_empty_list():
    """Test sorting an empty list"""
    assert counting_sort([]) == []

def test_single_element():
    """Test sorting a list with a single element"""
    assert counting_sort([5]) == [5]

def test_already_sorted():
    """Test sorting an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert counting_sort(arr) == arr

def test_reverse_sorted():
    """Test sorting a reverse sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert counting_sort(arr) == [1, 2, 3, 4, 5]

def test_duplicate_elements():
    """Test sorting a list with multiple duplicate elements"""
    arr = [3, 3, 3, 1, 1, 4, 4, 2]
    assert counting_sort(arr) == [1, 1, 2, 3, 3, 3, 4, 4]

def test_invalid_input_type():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        counting_sort("not a list")
    with pytest.raises(TypeError):
        counting_sort(123)

def test_negative_numbers():
    """Test handling of negative numbers"""
    with pytest.raises(ValueError):
        counting_sort([1, 2, -3, 4])

def test_non_integer_elements():
    """Test handling of non-integer elements"""
    with pytest.raises(ValueError):
        counting_sort([1, 2, 3.5, 4])
    with pytest.raises(ValueError):
        counting_sort([1, 2, "3", 4])