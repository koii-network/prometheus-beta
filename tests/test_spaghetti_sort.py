import pytest
from src.spaghetti_sort import spaghetti_sort

def test_spaghetti_sort_basic():
    """Test sorting a basic list of integers"""
    input_list = [5, 2, 8, 12, 1, 6]
    expected = [1, 2, 5, 6, 8, 12]
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
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
    expected = [1, 1, 2, 3, 4, 5, 5, 6, 9]
    assert spaghetti_sort(input_list) == expected

def test_spaghetti_sort_with_floats():
    """Test sorting a list of floating-point numbers"""
    input_list = [3.14, 2.71, 1.41, 0.58]
    expected = [0.58, 1.41, 2.71, 3.14]
    assert spaghetti_sort(input_list) == expected

def test_spaghetti_sort_invalid_input():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError):
        spaghetti_sort("not a list")

def test_spaghetti_sort_uncomparable_elements():
    """Test that ValueError is raised for uncomparable elements"""
    with pytest.raises(ValueError):
        spaghetti_sort([1, 2, "a", 3])