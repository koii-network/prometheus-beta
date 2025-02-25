import pytest
from src.arithmetic_sort import arithmetic_sort

def test_basic_sorting():
    """Test sorting a list of positive integers"""
    input_list = [5, 2, 9, 1, 7]
    expected = [1, 2, 5, 7, 9]
    assert arithmetic_sort(input_list) == expected

def test_already_sorted_list():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert arithmetic_sort(input_list) == input_list

def test_reverse_sorted_list():
    """Test sorting a list in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    expected = [1, 2, 3, 4, 5]
    assert arithmetic_sort(input_list) == expected

def test_list_with_duplicates():
    """Test sorting a list with duplicate values"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6]
    expected = [1, 1, 2, 3, 4, 5, 6, 9]
    assert arithmetic_sort(input_list) == expected

def test_empty_list():
    """Test sorting an empty list"""
    assert arithmetic_sort([]) == []

def test_single_element_list():
    """Test sorting a list with a single element"""
    input_list = [42]
    assert arithmetic_sort(input_list) == input_list

def test_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-5, 2, -10, 0, 7]
    expected = [-10, -5, 0, 2, 7]
    assert arithmetic_sort(input_list) == expected

def test_input_type_validation():
    """Test that non-list inputs raise TypeError"""
    with pytest.raises(TypeError):
        arithmetic_sort(42)
    with pytest.raises(TypeError):
        arithmetic_sort("not a list")

def test_non_integer_elements():
    """Test that lists with non-integer elements raise TypeError"""
    with pytest.raises(TypeError):
        arithmetic_sort([1, 2, 3, "4"])
    with pytest.raises(TypeError):
        arithmetic_sort([1, 2.5, 3])