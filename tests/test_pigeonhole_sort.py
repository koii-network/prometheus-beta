import pytest
from src.pigeonhole_sort import pigeonhole_sort

def test_basic_sorting():
    """Test basic integer sorting"""
    arr = [8, 3, 2, 7, 4, 6, 8]
    assert pigeonhole_sort(arr) == [2, 3, 4, 6, 7, 8, 8]

def test_already_sorted():
    """Test list that is already sorted"""
    arr = [1, 2, 3, 4, 5]
    assert pigeonhole_sort(arr) == [1, 2, 3, 4, 5]

def test_reverse_sorted():
    """Test list sorted in reverse order"""
    arr = [5, 4, 3, 2, 1]
    assert pigeonhole_sort(arr) == [1, 2, 3, 4, 5]

def test_empty_list():
    """Test empty list"""
    arr = []
    assert pigeonhole_sort(arr) == []

def test_single_element():
    """Test list with a single element"""
    arr = [42]
    assert pigeonhole_sort(arr) == [42]

def test_duplicate_elements():
    """Test list with duplicate elements"""
    arr = [3, 3, 3, 1, 1, 2]
    assert pigeonhole_sort(arr) == [1, 1, 2, 3, 3, 3]

def test_negative_numbers():
    """Test list with negative numbers"""
    arr = [-5, -2, -8, -1, -3]
    assert pigeonhole_sort(arr) == [-8, -5, -3, -2, -1]

def test_mixed_positive_negative():
    """Test list with mixed positive and negative numbers"""
    arr = [5, -3, 0, 2, -7, 1]
    assert pigeonhole_sort(arr) == [-7, -3, 0, 1, 2, 5]

def test_invalid_input_type():
    """Test raising TypeError for non-list input"""
    with pytest.raises(TypeError):
        pigeonhole_sort("not a list")

def test_non_integer_elements():
    """Test raising ValueError for non-integer elements"""
    with pytest.raises(ValueError):
        pigeonhole_sort([1, 2, 'a', 3])