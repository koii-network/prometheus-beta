import pytest
from src.linear_search import linear_search

def test_linear_search():
    # Test finding an element in the middle of the list
    assert linear_search([1, 2, 3, 4, 5], 3) == 2
    
    # Test finding an element at the beginning of the list
    assert linear_search([1, 2, 3, 4, 5], 1) == 0
    
    # Test finding an element at the end of the list
    assert linear_search([1, 2, 3, 4, 5], 5) == 4
    
    # Test element not in the list
    assert linear_search([1, 2, 3, 4, 5], 6) == -1
    
    # Test with an empty list
    assert linear_search([], 1) == -1
    
    # Test with strings
    assert linear_search(['apple', 'banana', 'cherry'], 'banana') == 1
    
    # Test with mixed types of elements
    assert linear_search([1, 'two', 3.0, True], 'two') == 1

def test_linear_search_edge_cases():
    # Test with None values
    assert linear_search([None, 1, 2, 3], None) == 0
    
    # Test with list of None values
    assert linear_search([None, None, None], None) == 0

def test_linear_search_error_handling():
    # Verify function works with unsortable types
    class CustomClass:
        def __init__(self, value):
            self.value = value
        
        def __eq__(self, other):
            return self.value == other
    
    obj1 = CustomClass(1)
    obj2 = CustomClass(2)
    obj3 = CustomClass(3)
    
    assert linear_search([obj1, obj2, obj3], 2) == 1