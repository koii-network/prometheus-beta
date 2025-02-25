import pytest
from src.counting_sort import counting_sort

def test_basic_sorting():
    """Test basic sorting of a list of non-negative integers"""
    assert counting_sort([4, 2, 2, 8, 3, 3, 1]) == [1, 2, 2, 3, 3, 4, 8]

def test_empty_list():
    """Test sorting an empty list"""
    assert counting_sort([]) == []

def test_single_element_list():
    """Test sorting a list with a single element"""
    assert counting_sort([5]) == [5]

def test_already_sorted_list():
    """Test a list that is already sorted"""
    assert counting_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_list_with_duplicates():
    """Test a list with multiple duplicate elements"""
    assert counting_sort([5, 5, 5, 2, 2, 1, 1]) == [1, 1, 2, 2, 5, 5, 5]

def test_zero_in_list():
    """Test a list containing zero"""
    assert counting_sort([0, 3, 2, 1]) == [0, 1, 2, 3]

def test_invalid_input_negative_numbers():
    """Test that a ValueError is raised for negative numbers"""
    with pytest.raises(ValueError, match="Counting sort only works with non-negative integers"):
        counting_sort([-1, 2, 3])

def test_invalid_input_non_integers():
    """Test that a TypeError is raised for non-integer elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        counting_sort([1, 2, '3'])

def test_invalid_input_not_a_list():
    """Test that a TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError, match="Input must be a list"):
        counting_sort("not a list")

def test_large_numbers():
    """Test sorting a list with larger numbers"""
    large_list = [1000, 10, 100, 1, 10000, 100000]
    assert counting_sort(large_list) == [1, 10, 100, 1000, 10000, 100000]