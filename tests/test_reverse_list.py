import pytest
from src.reverse_list import reverse_list

def test_reverse_list_normal():
    """Test reversing a list of integers"""
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

def test_reverse_list_negative_numbers():
    """Test reversing a list with negative numbers"""
    input_list = [-1, -2, -3, -4, -5]
    expected = [-5, -4, -3, -2, -1]
    assert reverse_list(input_list) == expected

def test_reverse_list_mixed_numbers():
    """Test reversing a list with mixed positive and negative numbers"""
    input_list = [-10, 0, 5, 100, -5]
    expected = [-5, 100, 5, 0, -10]
    assert reverse_list(input_list) == expected

def test_original_list_unchanged():
    """Test that the original list is not modified"""
    input_list = [1, 2, 3, 4, 5]
    original_copy = input_list.copy()
    reverse_list(input_list)
    assert input_list == original_copy