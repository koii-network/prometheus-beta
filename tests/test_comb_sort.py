import pytest
from src.comb_sort import comb_sort

def test_comb_sort_basic_list():
    """Test sorting a basic list of integers."""
    input_list = [64, 34, 25, 12, 22, 11, 90]
    expected = sorted(input_list)
    assert comb_sort(input_list) == expected

def test_comb_sort_already_sorted():
    """Test sorting a list that is already sorted."""
    input_list = [1, 2, 3, 4, 5]
    assert comb_sort(input_list) == input_list

def test_comb_sort_reverse_sorted():
    """Test sorting a list in reverse order."""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert comb_sort(input_list) == expected

def test_comb_sort_with_duplicates():
    """Test sorting a list with duplicate elements."""
    input_list = [4, 2, 2, 8, 3, 3, 1]
    expected = sorted(input_list)
    assert comb_sort(input_list) == expected

def test_comb_sort_empty_list():
    """Test sorting an empty list."""
    assert comb_sort([]) == []

def test_comb_sort_single_element():
    """Test sorting a list with a single element."""
    input_list = [42]
    assert comb_sort(input_list) == input_list

def test_comb_sort_with_floats():
    """Test sorting a list of floating-point numbers."""
    input_list = [3.14, 2.71, 1.41, 0.58]
    expected = sorted(input_list)
    assert comb_sort(input_list) == expected

def test_comb_sort_with_negative_numbers():
    """Test sorting a list with negative numbers."""
    input_list = [-4, 1, -9, 0, 2, -1]
    expected = sorted(input_list)
    assert comb_sort(input_list) == expected

def test_comb_sort_invalid_input():
    """Test that TypeError is raised for non-list input."""
    with pytest.raises(TypeError):
        comb_sort("not a list")
    
    with pytest.raises(TypeError):
        comb_sort(123)
    
    with pytest.raises(TypeError):
        comb_sort(None)