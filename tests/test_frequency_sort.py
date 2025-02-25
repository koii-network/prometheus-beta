import pytest
from src.frequency_sort import sort_by_frequency

def test_sort_by_frequency_basic():
    """Test basic frequency sorting"""
    input_list = [1, 1, 2, 2, 2, 3]
    expected = [3, 1, 1, 2, 2, 2]
    assert sort_by_frequency(input_list) == expected

def test_sort_by_frequency_empty_list():
    """Test sorting an empty list"""
    assert sort_by_frequency([]) == []

def test_sort_by_frequency_single_element():
    """Test list with a single element"""
    assert sort_by_frequency([5]) == [5]

def test_sort_by_frequency_same_frequency():
    """Test list where multiple elements have same frequency"""
    input_list = [1, 2, 3, 1, 2, 3]
    expected = [1, 2, 3, 1, 2, 3]
    assert sort_by_frequency(input_list) == expected

def test_sort_by_frequency_negative_numbers():
    """Test sorting with negative numbers"""
    input_list = [-1, -1, 2, 2, 3]
    expected = [3, -1, -1, 2, 2]
    assert sort_by_frequency(input_list) == expected

def test_sort_by_frequency_large_list():
    """Test sorting a larger list with varied frequencies"""
    input_list = [4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1]
    expected = [2, 2, 2, 3, 3, 1, 1, 1, 1, 4, 4, 4]
    assert sort_by_frequency(input_list) == expected