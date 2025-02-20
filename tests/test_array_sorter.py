import pytest
from src.array_sorter import sort_array_with_even_squares

def test_sort_array_with_even_squares_basic():
    """Test basic functionality of the sorting function"""
    input_arr = [3, 2, 4, 1, 5]
    expected = [1, 3, 5, 16, 4]
    assert sort_array_with_even_squares(input_arr) == expected

def test_sort_array_with_even_squares_all_even():
    """Test array with only even numbers"""
    input_arr = [6, 2, 4, 8]
    expected = [2, 4, 36, 64]
    assert sort_array_with_even_squares(input_arr) == expected

def test_sort_array_with_even_squares_all_odd():
    """Test array with only odd numbers"""
    input_arr = [3, 5, 1, 7]
    expected = [1, 3, 5, 7]
    assert sort_array_with_even_squares(input_arr) == expected

def test_sort_array_with_even_squares_empty():
    """Test empty input array"""
    input_arr = []
    expected = []
    assert sort_array_with_even_squares(input_arr) == expected

def test_sort_array_with_even_squares_negative_numbers():
    """Test array with negative numbers"""
    input_arr = [-3, -2, 4, 1, 5]
    expected = [-3, 1, 5, 16, 4]
    assert sort_array_with_even_squares(input_arr) == expected