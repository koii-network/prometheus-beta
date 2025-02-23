import pytest
from src.list_utils import remove_unique_elements

def test_remove_unique_elements_basic():
    # Test basic case with duplicates
    assert sorted(remove_unique_elements([1, 2, 2, 3, 4, 4, 5])) == [2, 4]

def test_remove_unique_elements_no_duplicates():
    # Test list with no duplicates
    assert remove_unique_elements([1, 2, 3, 4, 5]) == []

def test_remove_unique_elements_all_duplicates():
    # Test list with all elements duplicated
    assert sorted(remove_unique_elements([1, 1, 2, 2, 3, 3])) == [1, 2, 3]

def test_remove_unique_elements_empty_list():
    # Test empty list
    assert remove_unique_elements([]) == []

def test_remove_unique_elements_multiple_duplicates():
    # Test list with multiple duplicates of same element
    assert sorted(remove_unique_elements([1, 1, 1, 2, 2, 3, 4, 4, 4, 4])) == [1, 2, 4]

def test_remove_unique_elements_large_input():
    # Test larger input with various duplicates
    input_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6]
    assert sorted(remove_unique_elements(input_list)) == [2, 3, 4, 5]