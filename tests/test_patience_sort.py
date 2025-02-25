import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from patience_sort import patience_sort

def test_patience_sort_basic():
    """Test basic sorting of integers"""
    assert patience_sort([5, 2, 8, 1, 9]) == [1, 2, 5, 8, 9]

def test_patience_sort_empty_list():
    """Test sorting an empty list"""
    assert patience_sort([]) == []

def test_patience_sort_single_element():
    """Test sorting a list with a single element"""
    assert patience_sort([42]) == [42]

def test_patience_sort_already_sorted():
    """Test sorting an already sorted list"""
    assert patience_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_patience_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    assert patience_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_patience_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    assert patience_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]) == [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

def test_patience_sort_with_floats():
    """Test sorting a list of floats"""
    assert patience_sort([3.14, 2.71, 1.41, 0.58]) == [0.58, 1.41, 2.71, 3.14]

def test_patience_sort_with_strings():
    """Test sorting a list of strings"""
    assert patience_sort(['banana', 'apple', 'cherry', 'date']) == ['apple', 'banana', 'cherry', 'date']

def test_patience_sort_invalid_input():
    """Test that TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError):
        patience_sort("not a list")

def test_patience_sort_uncomparable_elements():
    """Test sorting with elements that cannot be compared"""
    class UncomparableClass:
        pass
    
    with pytest.raises(TypeError):
        patience_sort([UncomparableClass(), UncomparableClass()])