import pytest
from src.symmetric_difference import symmetric_difference

def test_symmetric_difference_basic():
    """Test basic symmetric difference"""
    assert sorted(symmetric_difference([1, 2, 3], [3, 4, 5])) == [1, 2, 4, 5]

def test_symmetric_difference_empty_lists():
    """Test with empty lists"""
    assert symmetric_difference([], []) == []

def test_symmetric_difference_one_empty_list():
    """Test with one empty list"""
    assert sorted(symmetric_difference([1, 2, 3], [])) == [1, 2, 3]

def test_symmetric_difference_identical_lists():
    """Test with identical lists"""
    assert symmetric_difference([1, 2, 3], [1, 2, 3]) == []

def test_symmetric_difference_with_duplicates():
    """Test with lists containing duplicates"""
    assert sorted(symmetric_difference([1, 1, 2, 3], [3, 4, 4, 5])) == [1, 2, 4, 5]

def test_symmetric_difference_different_types():
    """Test with lists of different types"""
    assert sorted(symmetric_difference([1, 'a'], ['a', 2])) == [1, 2]