import pytest
from src.symmetric_difference import symmetric_difference

def test_symmetric_difference_basic():
    """Test basic symmetric difference scenario"""
    list1 = [1, 2, 3]
    list2 = [3, 4, 5]
    result = symmetric_difference(list1, list2)
    assert set(result) == {1, 2, 4, 5}

def test_symmetric_difference_empty_lists():
    """Test symmetric difference with empty lists"""
    list1 = []
    list2 = []
    result = symmetric_difference(list1, list2)
    assert result == []

def test_symmetric_difference_one_empty_list():
    """Test symmetric difference with one empty list"""
    list1 = [1, 2, 3]
    list2 = []
    result = symmetric_difference(list1, list2)
    assert set(result) == {1, 2, 3}

def test_symmetric_difference_duplicate_elements():
    """Test symmetric difference with duplicate elements"""
    list1 = [1, 1, 2, 3]
    list2 = [3, 4, 4, 5]
    result = symmetric_difference(list1, list2)
    assert set(result) == {1, 2, 4, 5}

def test_symmetric_difference_identical_lists():
    """Test symmetric difference with identical lists"""
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    result = symmetric_difference(list1, list2)
    assert result == []

def test_symmetric_difference_non_numeric():
    """Test symmetric difference with non-numeric types"""
    list1 = ['a', 'b', 'c']
    list2 = ['b', 'c', 'd']
    result = symmetric_difference(list1, list2)
    assert set(result) == {'a', 'd'}