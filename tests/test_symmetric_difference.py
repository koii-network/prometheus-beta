import pytest
from src.symmetric_difference import symmetric_difference

def test_symmetric_difference_basic():
    """Test basic symmetric difference scenario"""
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    result = symmetric_difference(list1, list2)
    assert set(result) == {1, 2, 5, 6}

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

def test_symmetric_difference_no_overlap():
    """Test symmetric difference with no overlapping elements"""
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    result = symmetric_difference(list1, list2)
    assert set(result) == {1, 2, 3, 4, 5, 6}

def test_symmetric_difference_duplicate_elements():
    """Test symmetric difference with duplicate elements"""
    list1 = [1, 2, 2, 3, 3]
    list2 = [2, 3, 4, 4, 5]
    result = symmetric_difference(list1, list2)
    assert set(result) == {1, 4, 5}

def test_symmetric_difference_type_preservation():
    """Test that the return type is a list"""
    list1 = [1, 2, 3]
    list2 = [3, 4, 5]
    result = symmetric_difference(list1, list2)
    assert isinstance(result, list)