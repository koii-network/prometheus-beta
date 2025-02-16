import pytest
from src.tournament_sort import tournament_sort

def test_tournament_sort_basic():
    """Test sorting a basic list of integers."""
    input_list = [5, 2, 9, 1, 7, 6]
    expected = sorted(input_list)
    assert tournament_sort(input_list) == expected

def test_tournament_sort_empty_list():
    """Test sorting an empty list."""
    assert tournament_sort([]) == []

def test_tournament_sort_single_element():
    """Test sorting a list with a single element."""
    input_list = [42]
    assert tournament_sort(input_list) == input_list

def test_tournament_sort_negative_numbers():
    """Test sorting a list with negative numbers."""
    input_list = [-5, -2, -9, -1, -7, -6]
    expected = sorted(input_list)
    assert tournament_sort(input_list) == expected

def test_tournament_sort_mixed_numbers():
    """Test sorting a list with mixed positive and negative numbers."""
    input_list = [5, -2, 9, -1, 7, 6]
    expected = sorted(input_list)
    assert tournament_sort(input_list) == expected

def test_tournament_sort_duplicate_numbers():
    """Test sorting a list with duplicate numbers."""
    input_list = [5, 2, 5, 1, 7, 2]
    expected = sorted(input_list)
    assert tournament_sort(input_list) == expected

def test_tournament_sort_already_sorted():
    """Test sorting an already sorted list."""
    input_list = [1, 2, 3, 4, 5]
    assert tournament_sort(input_list) == input_list

def test_tournament_sort_reverse_sorted():
    """Test sorting a reverse-sorted list."""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert tournament_sort(input_list) == expected

def test_tournament_sort_original_list_unchanged():
    """Ensure the original list is not modified."""
    input_list = [5, 2, 9, 1, 7, 6]
    original_copy = input_list.copy()
    tournament_sort(input_list)
    assert input_list == original_copy