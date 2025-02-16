import pytest
from src.list_difference import find_list_difference

def test_find_list_difference_basic():
    list1 = [1, 2, 3, 4]
    list2 = [3, 4, 5, 6]
    
    result = find_list_difference(list1, list2)
    
    assert set(result['only_in_first']) == {1, 2}
    assert set(result['only_in_second']) == {5, 6}
    assert set(result['common']) == {3, 4}

def test_find_list_difference_identical_lists():
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    
    result = find_list_difference(list1, list2)
    
    assert result['only_in_first'] == []
    assert result['only_in_second'] == []
    assert set(result['common']) == {1, 2, 3}

def test_find_list_difference_empty_lists():
    list1 = []
    list2 = []
    
    result = find_list_difference(list1, list2)
    
    assert result['only_in_first'] == []
    assert result['only_in_second'] == []
    assert result['common'] == []

def test_find_list_difference_with_duplicates():
    list1 = [1, 1, 2, 3, 3]
    list2 = [2, 2, 3, 4, 4]
    
    result = find_list_difference(list1, list2)
    
    assert set(result['only_in_first']) == {1}
    assert set(result['only_in_second']) == {4}
    assert set(result['common']) == {2, 3}

def test_find_list_difference_different_types():
    list1 = [1, 'a', 2, 'b']
    list2 = [1, 'a', 3, 'c']
    
    result = find_list_difference(list1, list2)
    
    assert set(result['only_in_first']) == {2, 'b'}
    assert set(result['only_in_second']) == {3, 'c'}
    assert set(result['common']) == {1, 'a'}