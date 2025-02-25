import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from cocktail_shaker_sort import cocktail_shaker_sort

def test_cocktail_shaker_sort_normal_list():
    """Test sorting a normal list of integers."""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert cocktail_shaker_sort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_cocktail_shaker_sort_already_sorted():
    """Test sorting an already sorted list."""
    arr = [1, 2, 3, 4, 5]
    assert cocktail_shaker_sort(arr) == [1, 2, 3, 4, 5]

def test_cocktail_shaker_sort_reverse_sorted():
    """Test sorting a reverse sorted list."""
    arr = [5, 4, 3, 2, 1]
    assert cocktail_shaker_sort(arr) == [1, 2, 3, 4, 5]

def test_cocktail_shaker_sort_empty_list():
    """Test sorting an empty list."""
    arr = []
    assert cocktail_shaker_sort(arr) == []

def test_cocktail_shaker_sort_single_element():
    """Test sorting a list with a single element."""
    arr = [42]
    assert cocktail_shaker_sort(arr) == [42]

def test_cocktail_shaker_sort_duplicate_elements():
    """Test sorting a list with duplicate elements."""
    arr = [4, 2, 2, 8, 3, 3, 1]
    assert cocktail_shaker_sort(arr) == [1, 2, 2, 3, 3, 4, 8]

def test_cocktail_shaker_sort_negative_numbers():
    """Test sorting a list with negative numbers."""
    arr = [-4, 1, -9, 0, 5, -2]
    assert cocktail_shaker_sort(arr) == [-9, -4, -2, 0, 1, 5]

def test_cocktail_shaker_sort_non_list_input():
    """Test that a TypeError is raised for non-list input."""
    with pytest.raises(TypeError):
        cocktail_shaker_sort("not a list")

def test_cocktail_shaker_sort_uncomparable_elements():
    """Test that a ValueError is raised for uncomparable elements."""
    with pytest.raises(ValueError):
        cocktail_shaker_sort([1, 'a', 2])

def test_cocktail_shaker_sort_original_list_modified():
    """Test that the original list is modified in-place."""
    arr = [5, 2, 9, 1, 7]
    result = cocktail_shaker_sort(arr)
    assert arr == [1, 2, 5, 7, 9]
    assert result == [1, 2, 5, 7, 9]