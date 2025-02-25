import pytest
from src.comb_sort import comb_sort

def test_comb_sort_regular_list():
    """Test sorting a regular list of integers."""
    arr = [64, 34, 25, 12, 22, 11, 90]
    assert comb_sort(arr) == [11, 12, 22, 25, 34, 64, 90]

def test_comb_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    arr = [1, 2, 3, 4, 5]
    assert comb_sort(arr) == [1, 2, 3, 4, 5]

def test_comb_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    arr = [5, 4, 3, 2, 1]
    assert comb_sort(arr) == [1, 2, 3, 4, 5]

def test_comb_sort_empty_list():
    """Test sorting an empty list."""
    arr = []
    assert comb_sort(arr) == []

def test_comb_sort_single_element():
    """Test sorting a list with a single element."""
    arr = [42]
    assert comb_sort(arr) == [42]

def test_comb_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    arr = [4, 2, 2, 8, 3, 3, 1]
    assert comb_sort(arr) == [1, 2, 2, 3, 3, 4, 8]

def test_comb_sort_with_negative_numbers():
    """Test sorting a list with negative numbers."""
    arr = [-4, 1, -9, 0, 5, -2]
    assert comb_sort(arr) == [-9, -4, -2, 0, 1, 5]

def test_comb_sort_invalid_input():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError):
        comb_sort("not a list")

def test_comb_sort_with_floats():
    """Test sorting a list of floating-point numbers."""
    arr = [3.14, 2.71, 1.41, 0.58]
    assert comb_sort(arr) == [0.58, 1.41, 2.71, 3.14]