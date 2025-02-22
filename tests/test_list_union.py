import pytest
from src.list_union import list_union

def test_list_union_basic():
    """Test basic list union functionality"""
    assert sorted(list_union([1, 2, 3], [3, 4, 5])) == [1, 2, 3, 4, 5]

def test_list_union_duplicates():
    """Test list union with duplicate elements"""
    assert sorted(list_union([1, 1, 2, 2], [2, 2, 3, 3])) == [1, 2, 3]

def test_list_union_empty_lists():
    """Test list union with empty lists"""
    assert list_union([], []) == []
    assert sorted(list_union([], [1, 2, 3])) == [1, 2, 3]
    assert sorted(list_union([1, 2, 3], [])) == [1, 2, 3]

def test_list_union_different_types():
    """Test list union with mixed types"""
    assert sorted(list_union([1, 'a'], ['b', 2])) == [1, 2, 'a', 'b']

def test_list_union_type_preservation():
    """Test that the function preserves the unique nature of the combination"""
    result = list_union([1, 2, 3], [3, 4, 5])
    assert len(result) == 5
    assert len(set(result)) == len(result)  # Ensures no duplicates