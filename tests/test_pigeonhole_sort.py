import pytest
from src.pigeonhole_sort import pigeonhole_sort

def test_basic_sorting():
    """Test sorting a simple list of integers"""
    input_list = [8, 3, 2, 7, 4, 6, 8]
    expected = [2, 3, 4, 6, 7, 8, 8]
    assert pigeonhole_sort(input_list) == expected

def test_already_sorted():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert pigeonhole_sort(input_list) == input_list

def test_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert pigeonhole_sort(input_list) == expected

def test_empty_list():
    """Test sorting an empty list"""
    assert pigeonhole_sort([]) == []

def test_single_element():
    """Test sorting a list with a single element"""
    input_list = [42]
    assert pigeonhole_sort(input_list) == input_list

def test_negative_numbers():
    """Test sorting list with negative numbers"""
    input_list = [-5, -2, -8, -1, -3]
    expected = [-8, -5, -3, -2, -1]
    assert pigeonhole_sort(input_list) == expected

def test_mixed_numbers():
    """Test sorting list with mixed positive and negative numbers"""
    input_list = [-3, 4, 0, -1, 2]
    expected = [-3, -1, 0, 2, 4]
    assert pigeonhole_sort(input_list) == expected

def test_duplicate_numbers():
    """Test sorting list with duplicate numbers"""
    input_list = [3, 3, 3, 1, 1, 2]
    expected = [1, 1, 2, 3, 3, 3]
    assert pigeonhole_sort(input_list) == expected

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        pigeonhole_sort("not a list")

def test_incomparable_elements():
    """Test that ValueError is raised for incomparable elements"""
    with pytest.raises(ValueError, match="List contains incomparable elements"):
        pigeonhole_sort([1, 2, "3", 4])