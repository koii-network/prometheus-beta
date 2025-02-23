import pytest
from src.tournament_sort import tournament_sort

def test_tournament_sort_empty_list():
    """Test sorting an empty list"""
    assert tournament_sort([]) == []

def test_tournament_sort_single_element():
    """Test sorting a list with a single element"""
    assert tournament_sort([5]) == [5]

def test_tournament_sort_numeric_list():
    """Test sorting a list of numbers"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    assert tournament_sort(input_list) == sorted(input_list)

def test_tournament_sort_string_list():
    """Test sorting a list of strings"""
    input_list = ["banana", "apple", "cherry", "date"]
    assert tournament_sort(input_list) == sorted(input_list)

def test_tournament_sort_with_key():
    """Test sorting with a custom key function"""
    input_list = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35}
    ]
    sorted_list = tournament_sort(input_list, key=lambda x: x["age"])
    assert sorted_list == sorted(input_list, key=lambda x: x["age"])

def test_tournament_sort_already_sorted():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert tournament_sort(input_list) == input_list

def test_tournament_sort_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    input_list = [5, 4, 3, 2, 1]
    assert tournament_sort(input_list) == sorted(input_list)

def test_tournament_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert tournament_sort(input_list) == sorted(input_list)

def test_tournament_sort_error_non_list():
    """Test that a TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        tournament_sort("not a list")

def test_tournament_sort_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-5, 3, -2, 0, 7, -1]
    assert tournament_sort(input_list) == sorted(input_list)