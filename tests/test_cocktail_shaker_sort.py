import pytest
from src.cocktail_shaker_sort import cocktail_shaker_sort

def test_cocktail_shaker_sort_normal_list():
    """Test sorting a normal list of integers."""
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = cocktail_shaker_sort(arr.copy())
    assert sorted_arr == sorted(arr)
    assert arr == sorted(arr)  # Ensure in-place sorting

def test_cocktail_shaker_sort_already_sorted():
    """Test sorting an already sorted list."""
    arr = [1, 2, 3, 4, 5]
    sorted_arr = cocktail_shaker_sort(arr.copy())
    assert sorted_arr == arr

def test_cocktail_shaker_sort_reverse_sorted():
    """Test sorting a reverse-sorted list."""
    arr = [5, 4, 3, 2, 1]
    sorted_arr = cocktail_shaker_sort(arr.copy())
    assert sorted_arr == sorted(arr)

def test_cocktail_shaker_sort_empty_list():
    """Test sorting an empty list."""
    arr = []
    sorted_arr = cocktail_shaker_sort(arr.copy())
    assert sorted_arr == []

def test_cocktail_shaker_sort_single_element():
    """Test sorting a list with a single element."""
    arr = [42]
    sorted_arr = cocktail_shaker_sort(arr.copy())
    assert sorted_arr == [42]

def test_cocktail_shaker_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_arr = cocktail_shaker_sort(arr.copy())
    assert sorted_arr == sorted(arr)

def test_cocktail_shaker_sort_invalid_input():
    """Test raising TypeError for non-list input."""
    with pytest.raises(TypeError, match="Input must be a list"):
        cocktail_shaker_sort("not a list")
    with pytest.raises(TypeError, match="Input must be a list"):
        cocktail_shaker_sort(123)
    with pytest.raises(TypeError, match="Input must be a list"):
        cocktail_shaker_sort(None)