import pytest
from src.list_utils import list_union

def test_list_union_basic():
    """Test basic union of two lists"""
    result = list_union([1, 2, 3], [3, 4, 5])
    assert result == [1, 2, 3, 4, 5]

def test_list_union_with_duplicates():
    """Test union with duplicate elements"""
    result = list_union([1, 2, 2, 3], [3, 3, 4, 5])
    assert result == [1, 2, 3, 4, 5]

def test_list_union_empty_lists():
    """Test union with empty lists"""
    result = list_union([], [])
    assert result == []

def test_list_union_one_empty_list():
    """Test union with one empty list"""
    result = list_union([1, 2, 3], [])
    assert result == [1, 2, 3]

def test_list_union_different_types():
    """Test union with different types of elements"""
    result = list_union([1, 'a', 2], ['b', 3, 1])
    assert result == [1, 'a', 2, 'b', 3]