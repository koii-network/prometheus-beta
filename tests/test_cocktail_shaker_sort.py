import pytest
from src.cocktail_shaker_sort import cocktail_shaker_sort

def test_cocktail_shaker_sort_basic():
    """Test basic sorting functionality."""
    assert cocktail_shaker_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]

def test_cocktail_shaker_sort_already_sorted():
    """Test sorting an already sorted list."""
    assert cocktail_shaker_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_cocktail_shaker_sort_reverse_sorted():
    """Test sorting a reverse sorted list."""
    assert cocktail_shaker_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_cocktail_shaker_sort_empty_list():
    """Test sorting an empty list."""
    assert cocktail_shaker_sort([]) == []

def test_cocktail_shaker_sort_single_element():
    """Test sorting a list with a single element."""
    assert cocktail_shaker_sort([42]) == [42]

def test_cocktail_shaker_sort_duplicate_elements():
    """Test sorting a list with duplicate elements."""
    assert cocktail_shaker_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_cocktail_shaker_sort_invalid_input():
    """Test that an error is raised for non-list input."""
    with pytest.raises(TypeError):
        cocktail_shaker_sort("not a list")

def test_cocktail_shaker_sort_preserves_original():
    """Test that the original list is not modified."""
    original = [3, 1, 4, 1, 5]
    cocktail_shaker_sort(original)
    assert original == [3, 1, 4, 1, 5]  # Original list should remain unchanged