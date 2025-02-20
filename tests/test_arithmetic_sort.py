import pytest
from src.arithmetic_sort import arithmetic_sort

def test_arithmetic_sort_normal_case():
    """Test sorting a normal list of integers."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list)
    assert arithmetic_sort(input_list) == expected

def test_arithmetic_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    assert arithmetic_sort(input_list) == input_list

def test_arithmetic_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert arithmetic_sort(input_list) == expected

def test_arithmetic_sort_with_duplicates():
    """Test sorting a list with duplicate values."""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    expected = sorted(input_list)
    assert arithmetic_sort(input_list) == expected

def test_arithmetic_sort_empty_list():
    """Test sorting an empty list."""
    input_list = []
    assert arithmetic_sort(input_list) == []

def test_arithmetic_sort_single_element():
    """Test sorting a list with a single element."""
    input_list = [42]
    assert arithmetic_sort(input_list) == [42]

def test_arithmetic_sort_negative_numbers():
    """Test sorting a list with negative numbers."""
    input_list = [-5, 3, -2, 0, 7, -10]
    expected = sorted(input_list)
    assert arithmetic_sort(input_list) == expected

def test_arithmetic_sort_original_list_unchanged():
    """Test that the original list remains unchanged."""
    input_list = [3, 1, 4, 1, 5]
    original_copy = input_list.copy()
    arithmetic_sort(input_list)
    assert input_list == original_copy