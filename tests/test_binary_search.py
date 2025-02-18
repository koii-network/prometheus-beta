import pytest
from src.binary_search import binary_search

def test_binary_search_normal_cases():
    # Test finding elements in different positions
    assert binary_search([1, 3, 5, 7, 9], 5) == 2
    assert binary_search([1, 3, 5, 7, 9], 1) == 0
    assert binary_search([1, 3, 5, 7, 9], 9) == 4

def test_binary_search_element_not_found():
    # Test when element is not in the list
    assert binary_search([1, 3, 5, 7, 9], 4) == -1
    assert binary_search([1, 3, 5, 7, 9], 0) == -1
    assert binary_search([1, 3, 5, 7, 9], 10) == -1

def test_binary_search_empty_list():
    # Test with an empty list
    assert binary_search([], 5) == -1

def test_binary_search_single_element_list():
    # Test with a single-element list
    assert binary_search([5], 5) == 0
    assert binary_search([5], 6) == -1

def test_binary_search_invalid_input():
    # Test with invalid input types
    with pytest.raises(TypeError):
        binary_search("not a list", 5)
    
    with pytest.raises(TypeError):
        binary_search(None, 5)

def test_binary_search_unsorted_list():
    # Test with unsorted list
    with pytest.raises(ValueError):
        binary_search([5, 3, 1, 4, 2], 3)