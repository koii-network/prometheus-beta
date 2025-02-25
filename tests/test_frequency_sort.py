import pytest
from src.frequency_sort import sort_by_frequency

def test_basic_frequency_sort():
    """Test basic frequency sorting"""
    assert sort_by_frequency([1, 1, 2, 2, 2, 3]) == [3, 1, 1, 2, 2, 2]

def test_empty_list():
    """Test sorting an empty list"""
    assert sort_by_frequency([]) == []

def test_single_element():
    """Test sorting a list with a single element"""
    assert sort_by_frequency([5]) == [5]

def test_all_same_frequency():
    """Test list where all elements have same frequency"""
    assert sort_by_frequency([1, 2, 3, 4]) == [1, 2, 3, 4]

def test_multiple_elements_same_frequency():
    """Test list with multiple elements having same frequency"""
    assert sort_by_frequency([4, 4, 5, 5, 3, 3]) == [4, 4, 5, 5, 3, 3]

def test_large_numbers():
    """Test with large numbers"""
    assert sort_by_frequency([1000, 1000, 2, 2, 3]) == [3, 1000, 1000, 2, 2]

def test_negative_numbers():
    """Test with negative numbers"""
    assert sort_by_frequency([-1, -1, 2, 2, 3]) == [3, -1, -1, 2, 2]