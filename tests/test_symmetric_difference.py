import pytest
from src.symmetric_difference import symmetric_difference

def test_symmetric_difference_basic():
    list1 = [1, 2, 3]
    list2 = [3, 4, 5]
    result = symmetric_difference(list1, list2)
    assert sorted(result) == [1, 2, 4, 5]

def test_symmetric_difference_empty_lists():
    list1 = []
    list2 = []
    result = symmetric_difference(list1, list2)
    assert result == []

def test_symmetric_difference_one_empty_list():
    list1 = [1, 2, 3]
    list2 = []
    result = symmetric_difference(list1, list2)
    assert sorted(result) == [1, 2, 3]

def test_symmetric_difference_no_overlap():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    result = symmetric_difference(list1, list2)
    assert sorted(result) == [1, 2, 3, 4, 5, 6]

def test_symmetric_difference_same_lists():
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    result = symmetric_difference(list1, list2)
    assert result == []

def test_symmetric_difference_with_duplicates():
    list1 = [1, 2, 2, 3, 3]
    list2 = [3, 4, 4, 5]
    result = symmetric_difference(list1, list2)
    assert sorted(result) == [1, 2, 4, 5]