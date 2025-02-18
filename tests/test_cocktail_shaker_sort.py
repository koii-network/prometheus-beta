import pytest
from src.cocktail_shaker_sort import cocktail_shaker_sort

def test_cocktail_shaker_sort_normal_list():
    """Test sorting a normal unsorted list."""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert cocktail_shaker_sort(arr) == sorted(arr)

def test_cocktail_shaker_sort_already_sorted():
    """Test sorting an already sorted list."""
    arr = [1, 2, 3, 4, 5]
    assert cocktail_shaker_sort(arr) == arr

def test_cocktail_shaker_sort_reverse_sorted():
    """Test sorting a reverse-sorted list."""
    arr = [5, 4, 3, 2, 1]
    assert cocktail_shaker_sort(arr) == sorted(arr)

def test_cocktail_shaker_sort_empty_list():
    """Test sorting an empty list."""
    arr = []
    assert cocktail_shaker_sort(arr) == []

def test_cocktail_shaker_sort_single_element():
    """Test sorting a list with a single element."""
    arr = [42]
    assert cocktail_shaker_sort(arr) == [42]

def test_cocktail_shaker_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert cocktail_shaker_sort(arr) == sorted(arr)

def test_cocktail_shaker_sort_invalid_input():
    """Test that a TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError):
        cocktail_shaker_sort("not a list")
    with pytest.raises(TypeError):
        cocktail_shaker_sort(123)
    with pytest.raises(TypeError):
        cocktail_shaker_sort(None)