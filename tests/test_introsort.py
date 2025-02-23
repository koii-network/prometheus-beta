import pytest
import random
from src.introsort import introsort

def test_empty_list():
    """Test sorting an empty list"""
    assert introsort([]) == []

def test_single_element():
    """Test sorting a list with a single element"""
    assert introsort([5]) == [5]

def test_already_sorted():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert introsort(input_list) == sorted(input_list)

def test_reverse_sorted():
    """Test sorting a reverse sorted list"""
    input_list = [5, 4, 3, 2, 1]
    assert introsort(input_list) == sorted(input_list)

def test_random_list():
    """Test sorting a random list"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert introsort(input_list) == sorted(input_list)

def test_duplicate_elements():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 3, 3, 1, 1, 4, 4, 2, 2]
    assert introsort(input_list) == sorted(input_list)

def test_large_random_list():
    """Test sorting a large random list"""
    input_list = [random.randint(-1000, 1000) for _ in range(1000)]
    assert introsort(input_list) == sorted(input_list)

def test_list_with_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-5, 3, -2, 0, 1, -7, 4]
    assert introsort(input_list) == sorted(input_list)

def test_original_list_unchanged():
    """Test that the original list is not modified"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6]
    original = input_list.copy()
    introsort(input_list)
    assert input_list == original