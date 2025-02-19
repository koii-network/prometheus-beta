import pytest
from src.frequency_sort import sort_by_frequency

def test_sort_by_frequency_basic():
    """Test basic frequency sorting"""
    input_list = [2, 3, 1, 2, 3, 3, 1, 2]
    expected = [1, 1, 2, 2, 2, 3, 3, 3]
    assert sort_by_frequency(input_list) == expected

def test_sort_by_frequency_unique_elements():
    """Test list with unique elements"""
    input_list = [5, 2, 8, 1, 3]
    expected = [5, 2, 8, 1, 3]  # Order preserved when all elements are unique
    assert sort_by_frequency(input_list) == expected

def test_sort_by_frequency_empty_list():
    """Test empty list"""
    assert sort_by_frequency([]) == []

def test_sort_by_frequency_single_element():
    """Test list with single element"""
    assert sort_by_frequency([42]) == [42]

def test_sort_by_frequency_negative_numbers():
    """Test with negative numbers"""
    input_list = [-1, -1, 2, 2, 3, 3, 3]
    expected = [-1, -1, 2, 2, 3, 3, 3]
    assert sort_by_frequency(input_list) == expected