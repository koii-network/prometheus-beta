import pytest
from src.frequency_sort import sort_by_frequency

def test_sort_by_frequency_basic():
    # Test basic frequency sorting
    input_list = [1, 1, 2, 2, 2, 3]
    expected = [3, 1, 1, 2, 2, 2]
    assert sort_by_frequency(input_list) == expected

def test_sort_by_frequency_with_equal_frequency():
    # Test sorting with elements of equal frequency
    input_list = [4, 6, 2, 2, 6, 4]
    expected = [2, 2, 4, 4, 6, 6]
    assert sort_by_frequency(input_list) == expected

def test_sort_by_frequency_empty_list():
    # Test with empty list
    assert sort_by_frequency([]) == []

def test_sort_by_frequency_single_element():
    # Test with single element list
    input_list = [5]
    assert sort_by_frequency(input_list) == [5]

def test_sort_by_frequency_all_unique():
    # Test with all unique elements
    input_list = [1, 2, 3, 4, 5]
    expected = [1, 2, 3, 4, 5]
    assert sort_by_frequency(input_list) == expected

def test_sort_by_frequency_complex_case():
    # More complex case with mixed frequencies
    input_list = [5, 5, 4, 4, 4, 3, 3, 2, 1]
    expected = [2, 1, 5, 5, 3, 3, 4, 4, 4]
    assert sort_by_frequency(input_list) == expected