import pytest
from src.symmetric_difference import symmetric_difference

def test_symmetric_difference_basic():
    """Test basic symmetric difference functionality"""
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    result = symmetric_difference(list1, list2)
    assert set(result) == {1, 2, 5, 6}

def test_symmetric_difference_empty_list():
    """Test with an empty list"""
    list1 = [1, 2, 3]
    list2 = []
    result = symmetric_difference(list1, list2)
    assert set(result) == {1, 2, 3}

def test_symmetric_difference_identical_lists():
    """Test when lists are identical"""
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    result = symmetric_difference(list1, list2)
    assert len(result) == 0

def test_symmetric_difference_no_overlap():
    """Test lists with no common elements"""
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    result = symmetric_difference(list1, list2)
    assert set(result) == {1, 2, 3, 4, 5, 6}

def test_symmetric_difference_with_duplicates():
    """Test lists with duplicate elements"""
    list1 = [1, 1, 2, 3, 3]
    list2 = [2, 3, 4, 4]
    result = symmetric_difference(list1, list2)
    assert set(result) == {1, 4}