import pytest
from collections import Counter
from src.frequency_sort import sort_by_frequency

def test_normal_case():
    """Test sorting with a mix of frequencies"""
    input_list = [5, 2, 3, 1, 1, 2, 5, 5, 5]
    expected = [3, 2, 2, 1, 1, 5, 5, 5, 5]
    assert sort_by_frequency(input_list) == expected

def test_empty_list():
    """Test sorting an empty list"""
    assert sort_by_frequency([]) == []

def test_single_element():
    """Test sorting a list with a single element"""
    assert sort_by_frequency([42]) == [42]

def test_all_same_frequency():
    """Test sorting when all elements have the same frequency"""
    input_list = [1, 2, 3, 4, 5]
    assert sort_by_frequency(input_list) == input_list

def test_complex_frequency_ordering():
    """Test more complex frequency sorting scenario"""
    input_list = [4, 6, 2, 2, 6, 4, 4, 4]
    result = sort_by_frequency(input_list)
    print(f"Result: {result}")
    print(f"Input: {input_list}")
    print(f"Freq Count: {Counter(input_list)}")
    expected = [2, 2, 6, 6, 4, 4, 4, 4]
    assert result == expected

def test_negative_numbers():
    """Test sorting with negative numbers"""
    input_list = [-1, -1, 2, 3, 3, 3, -1]
    expected = [2, -1, -1, -1, 3, 3, 3]
    assert sort_by_frequency(input_list) == expected