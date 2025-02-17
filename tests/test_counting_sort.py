import pytest
from src.counting_sort import counting_sort

def test_counting_sort_basic():
    """Test basic sorting functionality"""
    assert counting_sort([4, 2, 2, 8, 3, 3, 1]) == [1, 2, 2, 3, 3, 4, 8]

def test_counting_sort_empty_list():
    """Test sorting an empty list"""
    assert counting_sort([]) == []

def test_counting_sort_single_element():
    """Test sorting a list with a single element"""
    assert counting_sort([5]) == [5]

def test_counting_sort_already_sorted():
    """Test sorting an already sorted list"""
    assert counting_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_counting_sort_repeated_elements():
    """Test sorting a list with many repeated elements"""
    assert counting_sort([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]

def test_counting_sort_zero_elements():
    """Test sorting a list with zeros"""
    assert counting_sort([0, 0, 0, 0]) == [0, 0, 0, 0]

def test_invalid_input_type():
    """Test that a non-list input raises TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        counting_sort("not a list")

def test_non_integer_elements():
    """Test that non-integer elements raise TypeError"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        counting_sort([1, 2, "3", 4])

def test_negative_numbers():
    """Test that negative numbers raise ValueError"""
    with pytest.raises(ValueError, match="Counting sort only works with non-negative integers"):
        counting_sort([1, 2, -3, 4])