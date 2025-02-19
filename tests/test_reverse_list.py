import pytest
from src.reverse_list import reverse_list

def test_reverse_list_normal_case():
    """Test reversing a standard list of integers"""
    input_list = [1, 2, 3, 4, 5]
    expected = [5, 4, 3, 2, 1]
    assert reverse_list(input_list) == expected

def test_reverse_list_empty():
    """Test reversing an empty list"""
    input_list = []
    expected = []
    assert reverse_list(input_list) == expected

def test_reverse_list_single_element():
    """Test reversing a list with a single element"""
    input_list = [42]
    expected = [42]
    assert reverse_list(input_list) == expected

def test_reverse_list_with_duplicates():
    """Test reversing a list with duplicate elements"""
    input_list = [1, 2, 2, 3, 3, 1]
    expected = [1, 3, 3, 2, 2, 1]
    assert reverse_list(input_list) == expected

def test_reverse_list_returns_new_list():
    """Ensure the function returns a new list, not modifying the original"""
    input_list = [1, 2, 3]
    reversed_list = reverse_list(input_list)
    assert reversed_list != input_list
    assert reversed_list == [3, 2, 1]
    assert input_list == [1, 2, 3]  # Original list remains unchanged