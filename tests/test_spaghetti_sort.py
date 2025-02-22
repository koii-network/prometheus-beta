import pytest
from src.spaghetti_sort import spaghetti_sort

def test_spaghetti_sort_basic():
    """Test basic sorting functionality"""
    input_list = [5, 2, 9, 1, 7, 6]
    expected = sorted(input_list)
    assert spaghetti_sort(input_list) == expected

def test_spaghetti_sort_already_sorted():
    """Test list that is already sorted"""
    input_list = [1, 2, 3, 4, 5]
    assert spaghetti_sort(input_list) == input_list

def test_spaghetti_sort_reverse_sorted():
    """Test list in reverse order"""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert spaghetti_sort(input_list) == expected

def test_spaghetti_sort_empty_list():
    """Test empty list"""
    assert spaghetti_sort([]) == []

def test_spaghetti_sort_single_element():
    """Test list with a single element"""
    input_list = [42]
    assert spaghetti_sort(input_list) == input_list

def test_spaghetti_sort_duplicate_elements():
    """Test list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(input_list)
    assert spaghetti_sort(input_list) == expected

def test_spaghetti_sort_invalid_input():
    """Test invalid input type"""
    with pytest.raises(TypeError):
        spaghetti_sort("not a list")
    
    with pytest.raises(TypeError):
        spaghetti_sort(123)
    
    with pytest.raises(TypeError):
        spaghetti_sort(None)