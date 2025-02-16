import pytest
from src.list_union import find_list_union

def test_basic_list_union():
    # Test basic union of two lists
    list1 = [1, 2, 3]
    list2 = [3, 4, 5]
    assert find_list_union(list1, list2) == [1, 2, 3, 4, 5]

def test_list_union_with_duplicates():
    # Test union with duplicates
    list1 = [1, 2, 2, 3]
    list2 = [3, 4, 4, 5]
    assert find_list_union(list1, list2) == [1, 2, 3, 4, 5]

def test_list_union_empty_lists():
    # Test with empty lists
    list1 = []
    list2 = []
    assert find_list_union(list1, list2) == []

def test_list_union_one_empty_list():
    # Test when one list is empty
    list1 = [1, 2, 3]
    list2 = []
    assert find_list_union(list1, list2) == [1, 2, 3]

def test_list_union_string_lists():
    # Test with string lists
    list1 = ['a', 'b', 'c']
    list2 = ['c', 'd', 'e']
    assert find_list_union(list1, list2) == ['a', 'b', 'c', 'd', 'e']

def test_list_union_mixed_types():
    # Test with mixed types
    list1 = [1, 'a', 2]
    list2 = ['a', 3, 4]
    assert find_list_union(list1, list2) == [1, 'a', 2, 3, 4]