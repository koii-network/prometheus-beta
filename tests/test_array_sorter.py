import pytest
from src.array_sorter import sort_array_with_even_squares

def test_basic_sort():
    # Basic test with mixed numbers
    input_arr = [3, 1, 2, 4, 5]
    expected = [1, 3, 5, 4, 2]
    assert sort_array_with_even_squares(input_arr) == expected

def test_empty_array():
    # Test with empty array
    assert sort_array_with_even_squares([]) == []

def test_only_even_numbers():
    # Test with only even numbers
    input_arr = [6, 2, 4, 8]
    expected = [2, 4, 6, 8]
    assert sort_array_with_even_squares(input_arr) == expected

def test_only_odd_numbers():
    # Test with only odd numbers
    input_arr = [7, 3, 5, 1]
    expected = [1, 3, 5, 7]
    assert sort_array_with_even_squares(input_arr) == expected

def test_negative_numbers():
    # Test with negative numbers
    input_arr = [-3, -1, -2, -4, -5]
    expected = [-5, -3, -1, -4, -2]
    assert sort_array_with_even_squares(input_arr) == expected

def test_mixed_positive_negative():
    # Test with mixed positive and negative numbers
    input_arr = [3, -1, 2, -4, 5]
    expected = [-1, 3, 5, 2, -4]
    assert sort_array_with_even_squares(input_arr) == expected