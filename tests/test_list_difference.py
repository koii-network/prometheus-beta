import pytest
from src.list_difference import find_list_difference

def test_list_difference_basic():
    # Test with lists having some unique and some common elements
    result = find_list_difference([1, 2, 3], [3, 4, 5])
    assert set(result['only_in_first']) == {1, 2}
    assert set(result['only_in_second']) == {4, 5}
    assert set(result['common']) == {3}

def test_list_difference_empty_lists():
    # Test with empty lists
    result = find_list_difference([], [])
    assert result['only_in_first'] == []
    assert result['only_in_second'] == []
    assert result['common'] == []

def test_list_difference_identical_lists():
    # Test with identical lists
    result = find_list_difference([1, 2, 3], [1, 2, 3])
    assert result['only_in_first'] == []
    assert result['only_in_second'] == []
    assert set(result['common']) == {1, 2, 3}

def test_list_difference_no_common_elements():
    # Test with lists having no common elements
    result = find_list_difference([1, 2, 3], [4, 5, 6])
    assert set(result['only_in_first']) == {1, 2, 3}
    assert set(result['only_in_second']) == {4, 5, 6}
    assert result['common'] == []

def test_list_difference_different_types():
    # Test with lists of different types
    result = find_list_difference(['a', 'b', 'c'], ['b', 'c', 'd'])
    assert set(result['only_in_first']) == {'a'}
    assert set(result['only_in_second']) == {'d'}
    assert set(result['common']) == {'b', 'c'}

def test_list_difference_with_duplicates():
    # Test with lists containing duplicates
    result = find_list_difference([1, 1, 2, 3], [1, 3, 3, 4])
    assert set(result['only_in_first']) == {2}
    assert set(result['only_in_second']) == {4}
    assert set(result['common']) == {1, 3}