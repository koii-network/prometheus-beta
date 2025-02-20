import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_sorted_list():
    # Test case with sorted list containing duplicates
    input_list = [1, 1, 2, 3, 3, 4, 5, 5]
    expected_output = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_list) == expected_output

def test_remove_duplicates_no_duplicates():
    # Test case with a list that has no duplicates
    input_list = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_list) == input_list

def test_remove_duplicates_empty_list():
    # Test case with an empty list
    assert remove_duplicates([]) == []

def test_remove_duplicates_none_input():
    # Test case with None input
    assert remove_duplicates(None) == []

def test_remove_duplicates_single_element():
    # Test case with a single element
    input_list = [42]
    assert remove_duplicates(input_list) == [42]

def test_remove_duplicates_all_same():
    # Test case where all elements are the same
    input_list = [7, 7, 7, 7, 7]
    assert remove_duplicates(input_list) == [7]