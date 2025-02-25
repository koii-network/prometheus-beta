import pytest
from src.linear_search import linear_search

def test_linear_search_found():
    """Test finding an existing element in the list"""
    assert linear_search([1, 2, 3, 4, 5], 3) == 2
    assert linear_search([10, 20, 30, 40, 50], 20) == 1

def test_linear_search_not_found():
    """Test when the target is not in the list"""
    assert linear_search([1, 2, 3, 4, 5], 6) == -1
    assert linear_search([], 1) == -1

def test_linear_search_first_occurrence():
    """Test that the first occurrence is returned"""
    assert linear_search([1, 2, 2, 3, 2], 2) == 1

def test_linear_search_edge_cases():
    """Test edge cases like empty list, single element list"""
    assert linear_search([], 5) == -1
    assert linear_search([5], 5) == 0
    assert linear_search([5], 6) == -1