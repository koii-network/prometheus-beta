import pytest
from src.list_difference import find_list_difference

def test_list_difference_basic():
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    result = find_list_difference(list1, list2)
    assert set(result['added']) == {5, 6}
    assert set(result['removed']) == {1, 2}

def test_list_difference_empty_lists():
    list1 = []
    list2 = []
    result = find_list_difference(list1, list2)
    assert result['added'] == []
    assert result['removed'] == []

def test_list_difference_no_change():
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    result = find_list_difference(list1, list2)
    assert result['added'] == []
    assert result['removed'] == []

def test_list_difference_strings():
    list1 = ['apple', 'banana', 'cherry']
    list2 = ['banana', 'date', 'cherry']
    result = find_list_difference(list1, list2)
    assert set(result['added']) == {'date'}
    assert set(result['removed']) == {'apple'}

def test_list_difference_mixed_types():
    list1 = [1, 'a', True]
    list2 = [1, 'b', False]
    result = find_list_difference(list1, list2)
    assert set(result['added']) == {'b', False}
    assert set(result['removed']) == {'a', True}