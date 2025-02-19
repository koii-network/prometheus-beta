import pytest
from src.tournament_sort import tournament_sort

def test_tournament_sort_basic():
    """Test basic sorting functionality"""
    arr = [5, 2, 9, 1, 7, 6, 3]
    assert tournament_sort(arr) == sorted(arr)

def test_tournament_sort_empty_list():
    """Test sorting an empty list"""
    assert tournament_sort([]) == []

def test_tournament_sort_single_element():
    """Test sorting a single-element list"""
    arr = [42]
    assert tournament_sort(arr) == arr

def test_tournament_sort_already_sorted():
    """Test sorting an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert tournament_sort(arr) == arr

def test_tournament_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert tournament_sort(arr) == sorted(arr)

def test_tournament_sort_with_duplicates():
    """Test sorting with duplicate elements"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert tournament_sort(arr) == sorted(arr)

def test_tournament_sort_with_floats():
    """Test sorting with floating-point numbers"""
    arr = [3.14, 2.71, 1.41, 0.58, 2.23]
    assert tournament_sort(arr) == sorted(arr)

def test_tournament_sort_invalid_input():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        tournament_sort("not a list")
    
    with pytest.raises(TypeError):
        tournament_sort(123)

def test_tournament_sort_non_comparable():
    """Test handling of non-comparable elements"""
    with pytest.raises(TypeError):
        tournament_sort([1, "a", 3, "b"])
        
def test_tournament_sort_preserves_original():
    """Test that original list is not modified"""
    arr = [5, 2, 9, 1, 7]
    tournament_sort(arr)
    assert arr == [5, 2, 9, 1, 7]  # Original list should remain unchanged