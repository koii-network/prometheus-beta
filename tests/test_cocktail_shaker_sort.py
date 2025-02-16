import pytest
from src.cocktail_shaker_sort import cocktail_shaker_sort

def test_cocktail_shaker_sort_normal_list():
    """Test sorting a normal list of integers."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list)
    assert cocktail_shaker_sort(input_list) == expected

def test_cocktail_shaker_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    assert cocktail_shaker_sort(input_list) == input_list

def test_cocktail_shaker_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert cocktail_shaker_sort(input_list) == expected

def test_cocktail_shaker_sort_empty_list():
    """Test sorting an empty list."""
    input_list = []
    assert cocktail_shaker_sort(input_list) == []

def test_cocktail_shaker_sort_single_element():
    """Test sorting a list with a single element."""
    input_list = [42]
    assert cocktail_shaker_sort(input_list) == [42]

def test_cocktail_shaker_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    input_list = [4, 2, 2, 8, 3, 3, 1]
    expected = sorted(input_list)
    assert cocktail_shaker_sort(input_list) == expected

def test_cocktail_shaker_sort_preserves_original():
    """Test that the original list is not modified."""
    input_list = [5, 2, 9, 1, 7]
    original_copy = input_list.copy()
    cocktail_shaker_sort(input_list)
    assert input_list == original_copy

def test_cocktail_shaker_sort_invalid_input():
    """Test that TypeError is raised for non-list inputs."""
    with pytest.raises(TypeError):
        cocktail_shaker_sort("not a list")
    with pytest.raises(TypeError):
        cocktail_shaker_sort(123)
    with pytest.raises(TypeError):
        cocktail_shaker_sort(None)