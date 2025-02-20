import pytest
from src.arithmetic_sort import arithmetic_sort

def test_arithmetic_sort_basic():
    # Test sorting a basic list of positive integers
    input_list = [5, 2, 9, 1, 7]
    expected = [1, 2, 5, 7, 9]
    assert arithmetic_sort(input_list) == expected

def test_arithmetic_sort_already_sorted():
    # Test list that is already sorted
    input_list = [1, 2, 3, 4, 5]
    assert arithmetic_sort(input_list) == input_list

def test_arithmetic_sort_reverse_sorted():
    # Test list sorted in reverse order
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert arithmetic_sort(input_list) == expected

def test_arithmetic_sort_with_duplicates():
    # Test list with duplicate values
    input_list = [3, 1, 4, 1, 5, 9, 2, 6]
    expected = [1, 1, 2, 3, 4, 5, 6, 9]
    assert arithmetic_sort(input_list) == expected

def test_arithmetic_sort_single_element():
    # Test single element list
    input_list = [42]
    assert arithmetic_sort(input_list) == [42]

def test_arithmetic_sort_empty_list():
    # Test empty list
    input_list = []
    assert arithmetic_sort(input_list) == []

def test_arithmetic_sort_negative_numbers():
    # Test list with negative numbers
    input_list = [-3, 0, -1, 5, -2, 4]
    expected = [-3, -2, -1, 0, 4, 5]
    assert arithmetic_sort(input_list) == expected

def test_arithmetic_sort_preserves_original():
    # Test that original list is not modified
    input_list = [5, 2, 1, 4, 3]
    original_copy = input_list.copy()
    arithmetic_sort(input_list)
    assert input_list == original_copy