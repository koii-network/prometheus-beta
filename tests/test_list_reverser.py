import pytest
from src.list_reverser import reverse_list_with_stack

def test_reverse_list_normal():
    """Test reversing a normal list of integers"""
    input_list = [1, 2, 3, 4, 5]
    expected = [5, 4, 3, 2, 1]
    assert reverse_list_with_stack(input_list) == expected

def test_reverse_list_empty():
    """Test reversing an empty list"""
    assert reverse_list_with_stack([]) == []

def test_reverse_list_single_element():
    """Test reversing a list with a single element"""
    input_list = [42]
    assert reverse_list_with_stack(input_list) == [42]

def test_reverse_list_with_negative_numbers():
    """Test reversing a list with negative numbers"""
    input_list = [-1, -2, -3, -4, -5]
    expected = [-5, -4, -3, -2, -1]
    assert reverse_list_with_stack(input_list) == expected

def test_reverse_list_with_mixed_numbers():
    """Test reversing a list with mixed positive and negative numbers"""
    input_list = [-10, 0, 5, -3, 7]
    expected = [7, -3, 5, 0, -10]
    assert reverse_list_with_stack(input_list) == expected