import pytest
from src.pancake_sort import pancake_sort

def test_pancake_sort_basic():
    """Test basic sorting functionality"""
    assert pancake_sort([3, 2, 1]) == [1, 2, 3]
    assert pancake_sort([4, 2, 7, 1, 5, 3]) == [1, 2, 3, 4, 5, 7]

def test_pancake_sort_already_sorted():
    """Test when list is already sorted"""
    assert pancake_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_pancake_sort_reverse_sorted():
    """Test when list is in reverse order"""
    assert pancake_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_pancake_sort_duplicates():
    """Test list with duplicate elements"""
    assert pancake_sort([3, 3, 2, 1, 2]) == [1, 2, 2, 3, 3]

def test_pancake_sort_empty_list():
    """Test empty list"""
    assert pancake_sort([]) == []

def test_pancake_sort_single_element():
    """Test list with single element"""
    assert pancake_sort([42]) == [42]

def test_pancake_sort_negative_numbers():
    """Test list with negative numbers"""
    assert pancake_sort([-1, -5, 10, 0, 3]) == [-5, -1, 0, 3, 10]