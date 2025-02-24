import pytest
from src.counting_sort import counting_sort

def test_basic_sorting():
    """Test basic sorting functionality"""
    input_list = [4, 2, 2, 8, 3, 3, 1]
    assert counting_sort(input_list) == [1, 2, 2, 3, 3, 4, 8]

def test_empty_list():
    """Test sorting an empty list"""
    assert counting_sort([]) == []

def test_single_element():
    """Test sorting a list with a single element"""
    assert counting_sort([5]) == [5]

def test_already_sorted():
    """Test sorting a list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert counting_sort(input_list) == [1, 2, 3, 4, 5]

def test_reverse_sorted():
    """Test sorting a list in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    assert counting_sort(input_list) == [1, 2, 3, 4, 5]

def test_duplicate_elements():
    """Test sorting with multiple duplicate elements"""
    input_list = [3, 3, 3, 1, 1, 2, 2]
    assert counting_sort(input_list) == [1, 1, 2, 2, 3, 3, 3]

def test_input_type_error():
    """Test that TypeError is raised for non-list input"""
    with pytest.raises(TypeError, match="Input must be a list"):
        counting_sort("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list"):
        counting_sort(123)

def test_negative_number_error():
    """Test that ValueError is raised for negative numbers"""
    with pytest.raises(ValueError, match="List must contain only non-negative integers"):
        counting_sort([-1, 2, 3])
    
    with pytest.raises(ValueError, match="List must contain only non-negative integers"):
        counting_sort([1.5, 2, 3])

def test_zero_handling():
    """Test handling of zero in the list"""
    input_list = [0, 5, 3, 0, 2]
    assert counting_sort(input_list) == [0, 0, 2, 3, 5]