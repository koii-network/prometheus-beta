import pytest
from src.tournament_sort import tournament_sort

def test_tournament_sort_basic_integers():
    """Test sorting of basic integer list"""
    arr = [5, 2, 9, 1, 7, 6]
    assert tournament_sort(arr) == [1, 2, 5, 6, 7, 9]

def test_tournament_sort_already_sorted():
    """Test sorting of already sorted list"""
    arr = [1, 2, 3, 4, 5]
    assert tournament_sort(arr) == [1, 2, 3, 4, 5]

def test_tournament_sort_reverse_sorted():
    """Test sorting of reverse sorted list"""
    arr = [5, 4, 3, 2, 1]
    assert tournament_sort(arr) == [1, 2, 3, 4, 5]

def test_tournament_sort_single_element():
    """Test sorting of single element list"""
    arr = [42]
    assert tournament_sort(arr) == [42]

def test_tournament_sort_custom_comparator():
    """Test sorting with custom comparator (descending order)"""
    arr = [5, 2, 9, 1, 7, 6]
    assert tournament_sort(arr, lambda x, y: x > y) == [9, 7, 6, 5, 2, 1]

def test_tournament_sort_with_strings():
    """Test sorting of strings"""
    arr = ['banana', 'apple', 'cherry', 'date']
    assert tournament_sort(arr) == ['apple', 'banana', 'cherry', 'date']

def test_tournament_sort_raises_on_empty_list():
    """Test that ValueError is raised for empty list"""
    with pytest.raises(ValueError, match="Cannot sort an empty list"):
        tournament_sort([])

def test_tournament_sort_raises_on_invalid_input():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        tournament_sort("not a list")

def test_tournament_sort_does_not_modify_original():
    """Test that original list is not modified"""
    arr = [5, 2, 9, 1, 7, 6]
    tournament_sort(arr)
    assert arr == [5, 2, 9, 1, 7, 6]  # Original list unchanged

def test_tournament_sort_with_duplicates():
    """Test sorting list with duplicate elements"""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert tournament_sort(arr) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]