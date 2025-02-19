import pytest
from src.tournament_sort import tournament_sort

def test_tournament_sort_normal_list():
    """Test sorting a normal list of integers"""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list)
    assert tournament_sort(input_list) == expected

def test_tournament_sort_empty_list():
    """Test sorting an empty list"""
    assert tournament_sort([]) == []

def test_tournament_sort_single_element():
    """Test sorting a list with a single element"""
    assert tournament_sort([42]) == [42]

def test_tournament_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert tournament_sort(input_list) == input_list

def test_tournament_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert tournament_sort(input_list) == expected

def test_tournament_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(input_list)
    assert tournament_sort(input_list) == expected

def test_tournament_sort_with_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-5, 10, -3, 0, 7, -1]
    expected = sorted(input_list)
    assert tournament_sort(input_list) == expected

def test_tournament_sort_float_numbers():
    """Test sorting a list with floating-point numbers"""
    input_list = [3.14, 2.71, 1.41, 0.58]
    expected = sorted(input_list)
    assert tournament_sort(input_list) == expected

def test_tournament_sort_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        tournament_sort("not a list")
    with pytest.raises(TypeError):
        tournament_sort(123)
    with pytest.raises(TypeError):
        tournament_sort(None)