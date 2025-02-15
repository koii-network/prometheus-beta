import pytest
from src.counting_sort import counting_sort

def test_basic_sorting():
    """Test basic sorting of a list of positive integers"""
    assert counting_sort([4, 2, 2, 8, 3, 3, 1]) == [1, 2, 2, 3, 3, 4, 8]

def test_empty_list():
    """Test sorting an empty list"""
    assert counting_sort([]) == []

def test_single_element_list():
    """Test sorting a list with a single element"""
    assert counting_sort([5]) == [5]

def test_already_sorted_list():
    """Test sorting a list that is already sorted"""
    assert counting_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_list_with_duplicates():
    """Test sorting a list with multiple duplicate elements"""
    assert counting_sort([5, 5, 5, 2, 2, 1]) == [1, 2, 2, 5, 5, 5]

def test_zero_included():
    """Test sorting a list that includes zero"""
    assert counting_sort([0, 3, 1, 2]) == [0, 1, 2, 3]

def test_invalid_input_type():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        counting_sort("not a list")

def test_non_integer_elements():
    """Test that TypeError is raised for non-integer elements"""
    with pytest.raises(TypeError, match="All elements must be integers"):
        counting_sort([1, 2, "3", 4])

def test_negative_numbers():
    """Test that ValueError is raised for negative numbers"""
    with pytest.raises(ValueError, match="Counting sort only works with non-negative integers"):
        counting_sort([1, 2, -3, 4])