import pytest
from src.tournament_sort import tournament_sort

def test_tournament_sort_empty_list():
    """Test sorting an empty list"""
    assert tournament_sort([]) == []

def test_tournament_sort_single_element():
    """Test sorting a list with a single element"""
    assert tournament_sort([5]) == [5]

def test_tournament_sort_sorted_list():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert tournament_sort(input_list) == input_list

def test_tournament_sort_reverse_sorted_list():
    """Test sorting a reverse sorted list"""
    input_list = [5, 4, 3, 2, 1]
    assert tournament_sort(input_list) == [1, 2, 3, 4, 5]

def test_tournament_sort_random_list():
    """Test sorting a list with random elements"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    assert tournament_sort(input_list) == [11, 12, 22, 25, 34, 64, 90]

def test_tournament_sort_duplicate_elements():
    """Test sorting a list with duplicate elements"""
    input_list = [5, 2, 9, 1, 5, 6, 2]
    assert tournament_sort(input_list) == [1, 2, 2, 5, 5, 6, 9]

def test_tournament_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-5, 10, -3, 0, 7, -1]
    assert tournament_sort(input_list) == [-5, -3, -1, 0, 7, 10]

def test_tournament_sort_original_list_unchanged():
    """Test that the original list is not modified"""
    input_list = [5, 2, 9, 1, 3]
    tournament_sort(input_list)
    assert input_list == [5, 2, 9, 1, 3]