import pytest
from src.tournament_sort import tournament_sort

def test_tournament_sort_basic():
    """Test sorting a typical list of integers."""
    arr = [5, 2, 9, 1, 7, 6, 3]
    assert tournament_sort(arr) == sorted(arr)

def test_tournament_sort_empty_list():
    """Test sorting an empty list."""
    arr = []
    assert tournament_sort(arr) == []

def test_tournament_sort_single_element():
    """Test sorting a list with a single element."""
    arr = [42]
    assert tournament_sort(arr) == [42]

def test_tournament_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    arr = [1, 2, 3, 4, 5]
    assert tournament_sort(arr) == [1, 2, 3, 4, 5]

def test_tournament_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    arr = [5, 4, 3, 2, 1]
    assert tournament_sort(arr) == [1, 2, 3, 4, 5]

def test_tournament_sort_duplicate_elements():
    """Test sorting a list with duplicate elements."""
    arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert tournament_sort(arr) == sorted(arr)

def test_tournament_sort_with_negative_numbers():
    """Test sorting a list with negative numbers."""
    arr = [-5, 2, 0, -3, 7, 1, -1]
    assert tournament_sort(arr) == sorted(arr)

def test_tournament_sort_with_floats():
    """Test sorting a list with floating-point numbers."""
    arr = [3.14, 2.71, 1.41, 0.58, 2.23]
    assert tournament_sort(arr) == sorted(arr)

def test_tournament_sort_invalid_input():
    """Test that the function raises a TypeError for non-list inputs."""
    with pytest.raises(TypeError):
        tournament_sort("not a list")
    with pytest.raises(TypeError):
        tournament_sort(123)
    with pytest.raises(TypeError):
        tournament_sort(None)