import pytest
import random
from src.intro_sort import intro_sort

def test_intro_sort_empty_list():
    """Test sorting an empty list"""
    assert intro_sort([]) == []

def test_intro_sort_single_element():
    """Test sorting a list with a single element"""
    assert intro_sort([42]) == [42]

def test_intro_sort_already_sorted():
    """Test sorting an already sorted list"""
    sorted_list = [1, 2, 3, 4, 5]
    assert intro_sort(sorted_list) == sorted_list

def test_intro_sort_reverse_sorted():
    """Test sorting a reverse sorted list"""
    reverse_sorted = [5, 4, 3, 2, 1]
    assert intro_sort(reverse_sorted) == [1, 2, 3, 4, 5]

def test_intro_sort_random_list():
    """Test sorting a random list of integers"""
    original_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert intro_sort(original_list) == sorted(original_list)

def test_intro_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    list_with_duplicates = [3, 3, 3, 1, 1, 4, 4, 2, 2]
    assert intro_sort(list_with_duplicates) == sorted(list_with_duplicates)

def test_intro_sort_large_random_list():
    """Test sorting a large random list"""
    large_list = [random.randint(-1000, 1000) for _ in range(1000)]
    assert intro_sort(large_list) == sorted(large_list)

def test_intro_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    negative_list = [-5, -3, -1, -10, -7]
    assert intro_sort(negative_list) == sorted(negative_list)

def test_intro_sort_mixed_numbers():
    """Test sorting a list with mixed positive and negative numbers"""
    mixed_list = [-5, 3, 0, -1, 10, -7, 2]
    assert intro_sort(mixed_list) == sorted(mixed_list)

def test_intro_sort_invalid_input():
    """Test that an invalid input raises a TypeError"""
    with pytest.raises(TypeError):
        intro_sort("not a list")
    with pytest.raises(TypeError):
        intro_sort(123)
    with pytest.raises(TypeError):
        intro_sort(None)

def test_intro_sort_preserves_original_list():
    """Test that the original list is not modified"""
    original_list = [3, 1, 4, 1, 5, 9]
    copied_list = original_list.copy()
    sorted_list = intro_sort(original_list)
    assert original_list == copied_list
    assert sorted_list == sorted(original_list)