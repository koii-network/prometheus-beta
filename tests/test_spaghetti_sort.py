import pytest
from src.spaghetti_sort import spaghetti_sort

def test_spaghetti_sort_basic():
    """Test sorting a basic list of integers"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(input_list)
    assert spaghetti_sort(input_list) == expected

def test_spaghetti_sort_empty_list():
    """Test sorting an empty list"""
    assert spaghetti_sort([]) == []

def test_spaghetti_sort_single_element():
    """Test sorting a list with a single element"""
    assert spaghetti_sort([42]) == [42]

def test_spaghetti_sort_already_sorted():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert spaghetti_sort(input_list) == input_list

def test_spaghetti_sort_reverse_sorted():
    """Test sorting a list in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert spaghetti_sort(input_list) == expected

def test_spaghetti_sort_with_duplicates():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 3, 3, 1, 1, 2, 2]
    expected = [1, 1, 2, 2, 3, 3, 3]
    assert spaghetti_sort(input_list) == expected

def test_spaghetti_sort_invalid_input():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        spaghetti_sort("not a list")
    with pytest.raises(TypeError):
        spaghetti_sort(123)
    with pytest.raises(TypeError):
        spaghetti_sort(None)