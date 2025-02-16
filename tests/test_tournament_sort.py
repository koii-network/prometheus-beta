import pytest
from src.tournament_sort import tournament_sort

def test_tournament_sort_basic():
    """Test basic sorting functionality"""
    arr = [64, 34, 25, 12, 22, 11, 90]
    result = tournament_sort(arr)
    assert result == sorted(arr), "Should sort in ascending order"

def test_tournament_sort_already_sorted():
    """Test sorting an already sorted list"""
    arr = [1, 2, 3, 4, 5]
    result = tournament_sort(arr)
    assert result == arr, "Should return the same list when already sorted"

def test_tournament_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    arr = [5, 4, 3, 2, 1]
    result = tournament_sort(arr)
    assert result == sorted(arr), "Should correctly sort reverse-sorted list"

def test_tournament_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    arr = [4, 2, 2, 8, 3, 3, 1]
    result = tournament_sort(arr)
    assert result == sorted(arr), "Should handle duplicate elements"

def test_tournament_sort_empty_list():
    """Test sorting an empty list"""
    arr = []
    result = tournament_sort(arr)
    assert result == [], "Should return an empty list"

def test_tournament_sort_single_element():
    """Test sorting a single-element list"""
    arr = [42]
    result = tournament_sort(arr)
    assert result == arr, "Should return the same single-element list"

def test_tournament_sort_invalid_input():
    """Test handling of invalid input types"""
    with pytest.raises(TypeError):
        tournament_sort("not a list")
    
    with pytest.raises(TypeError):
        tournament_sort(123)

def test_tournament_sort_float_elements():
    """Test sorting list with float elements"""
    arr = [3.14, 2.71, 1.41, 0.58]
    result = tournament_sort(arr)
    assert result == sorted(arr), "Should handle float elements"