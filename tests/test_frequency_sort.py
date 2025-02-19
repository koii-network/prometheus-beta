import pytest
from src.frequency_sort import sort_by_frequency

def test_sort_by_frequency_basic():
    # Test case with different frequencies
    input_list = [5, 2, 3, 1, 1, 5, 5, 2]
    expected = [3, 2, 2, 5, 5, 5, 1, 1]
    assert sort_by_frequency(input_list) == expected

def test_sort_by_frequency_equal_frequency():
    # Test case where some elements have equal frequency
    input_list = [4, 4, 5, 5, 2, 2, 1, 1]
    expected = [1, 1, 2, 2, 4, 4, 5, 5]
    assert sort_by_frequency(input_list) == expected

def test_sort_by_frequency_empty_list():
    # Test with empty list
    assert sort_by_frequency([]) == []

def test_sort_by_frequency_single_element():
    # Test with a single element
    assert sort_by_frequency([42]) == [42]

def test_sort_by_frequency_all_same():
    # Test with all elements being the same
    input_list = [1, 1, 1, 1]
    assert sort_by_frequency(input_list) == [1, 1, 1, 1]