import pytest
from src.list_difference import find_list_difference

def test_list_difference_basic():
    # Test basic list difference
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    result = find_list_difference(list1, list2)
    assert sorted(result['added']) == [5, 6]
    assert sorted(result['removed']) == [1, 2]

def test_list_difference_empty_lists():
    # Test with empty lists
    list1 = []
    list2 = []
    result = find_list_difference(list1, list2)
    assert result['added'] == []
    assert result['removed'] == []

def test_list_difference_one_empty_list():
    # Test when one list is empty
    list1 = [1, 2, 3]
    list2 = []
    result = find_list_difference(list1, list2)
    assert result['added'] == []
    assert sorted(result['removed']) == [1, 2, 3]

def test_list_difference_string_lists():
    # Test with string lists
    list1 = ['apple', 'banana', 'cherry']
    list2 = ['banana', 'date', 'elderberry']
    result = find_list_difference(list1, list2)
    assert sorted(result['added']) == ['date', 'elderberry']
    assert sorted(result['removed']) == ['apple', 'cherry']

def test_list_difference_duplicate_elements():
    # Test with duplicate elements
    list1 = [1, 1, 2, 3, 3]
    list2 = [1, 2, 2, 4, 4]
    result = find_list_difference(list1, list2)
    assert sorted(result['added']) == [4]
    assert sorted(result['removed']) == [3]