import pytest
from src.binary_search import binary_search

def test_binary_search():
    # Test with multiple occurrences
    assert binary_search([1, 2, 2, 3, 4, 4, 4, 5], 2) == 1
    assert binary_search([1, 2, 2, 3, 4, 4, 4, 5], 4) == 4
    
    # Test with single occurrence
    assert binary_search([1, 2, 3, 4, 5], 3) == 2
    
    # Test with no occurrence
    assert binary_search([1, 2, 3, 4, 5], 6) == -1
    
    # Test with empty array
    assert binary_search([], 1) == -1
    
    # Test with invalid input
    assert binary_search([1, 2, 3], -1) == -1
    
    # Test with array of one element
    assert binary_search([1], 1) == 0
    assert binary_search([1], 2) == -1