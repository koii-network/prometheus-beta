import pytest
from src.sort_by_frequency import sort_by_frequency

def test_sort_by_frequency_basic():
    """Test basic frequency sorting"""
    input_list = [5, 2, 3, 1, 1, 2, 5, 5, 5]
    expected = [3, 2, 2, 1, 1, 5, 5, 5, 5]
    assert sort_by_frequency(input_list) == expected

def test_sort_by_frequency_with_negatives():
    """Test frequency sorting with negative numbers"""
    input_list = [-1, -1, 2, 2, 3, 3, 3, 4]
    expected = [4, -1, -1, 2, 2, 3, 3, 3]
    assert sort_by_frequency(input_list) == expected

def test_sort_by_frequency_empty_list():
    """Test with an empty list"""
    assert sort_by_frequency([]) == []

def test_sort_by_frequency_single_element():
    """Test with a single element list"""
    assert sort_by_frequency([42]) == [42]

def test_sort_by_frequency_all_unique():
    """Test with all unique elements"""
    input_list = [5, 4, 3, 2, 1]
    expected = [5, 4, 3, 2, 1]
    assert sort_by_frequency(input_list) == expected