import pytest
from src.list_difference import find_list_difference

def test_find_list_difference():
    # Test case 1: Lists with differences
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    result = find_list_difference(list1, list2)
    assert sorted(result['added']) == [5, 6]
    assert sorted(result['removed']) == [1, 2]

def test_find_list_difference_no_changes():
    # Test case 2: Identical lists
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    result = find_list_difference(list1, list2)
    assert result['added'] == []
    assert result['removed'] == []

def test_find_list_difference_empty_lists():
    # Test case 3: Empty lists
    list1 = []
    list2 = []
    result = find_list_difference(list1, list2)
    assert result['added'] == []
    assert result['removed'] == []

def test_find_list_difference_one_empty_list():
    # Test case 4: One list is empty
    list1 = [1, 2, 3]
    list2 = []
    result = find_list_difference(list1, list2)
    assert result['added'] == []
    assert sorted(result['removed']) == [1, 2, 3]

def test_find_list_difference_with_duplicates():
    # Test case 5: Lists with duplicates
    list1 = [1, 1, 2, 3, 3]
    list2 = [1, 2, 2, 4, 4]
    result = find_list_difference(list1, list2)
    assert sorted(result['added']) == [4]
    assert sorted(result['removed']) == [3]