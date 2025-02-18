import pytest
from src.patience_sort import patience_sort

def test_patience_sort_empty_list():
    """Test sorting an empty list"""
    assert patience_sort([]) == []

def test_patience_sort_single_element():
    """Test sorting a list with a single element"""
    assert patience_sort([5]) == [5]

def test_patience_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    arr = [1, 2, 3, 4, 5]
    assert patience_sort(arr) == arr

def test_patience_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    arr = [5, 4, 3, 2, 1]
    assert patience_sort(arr) == [1, 2, 3, 4, 5]

def test_patience_sort_random_integers():
    """Test sorting a list of random integers"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert patience_sort(arr) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_patience_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    arr = [3, 3, 3, 1, 1, 2, 2]
    assert patience_sort(arr) == [1, 1, 2, 2, 3, 3, 3]

def test_patience_sort_with_key_function():
    """Test sorting with a custom key function"""
    arr = [{'val': 5}, {'val': 2}, {'val': 8}, {'val': 1}]
    sorted_arr = patience_sort(arr, key=lambda x: x['val'])
    assert sorted_arr == [{'val': 1}, {'val': 2}, {'val': 5}, {'val': 8}]

def test_patience_sort_with_strings():
    """Test sorting a list of strings"""
    arr = ['banana', 'apple', 'cherry', 'date']
    assert patience_sort(arr) == ['apple', 'banana', 'cherry', 'date']

def test_patience_sort_with_floats():
    """Test sorting a list of floating-point numbers"""
    arr = [3.14, 2.71, 1.41, 0.58, 2.23]
    assert patience_sort(arr) == [0.58, 1.41, 2.23, 2.71, 3.14]