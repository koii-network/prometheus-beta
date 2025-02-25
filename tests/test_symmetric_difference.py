import pytest
from src.symmetric_difference import symmetric_difference

def test_symmetric_difference_basic():
    """Test basic symmetric difference scenario"""
    assert set(symmetric_difference([1, 2, 3], [3, 4, 5])) == {1, 2, 4, 5}

def test_symmetric_difference_empty_lists():
    """Test symmetric difference with empty lists"""
    assert symmetric_difference([], []) == []

def test_symmetric_difference_one_empty_list():
    """Test symmetric difference with one empty list"""
    assert set(symmetric_difference([1, 2, 3], [])) == {1, 2, 3}

def test_symmetric_difference_identical_lists():
    """Test symmetric difference with identical lists"""
    assert symmetric_difference([1, 2, 3], [1, 2, 3]) == []

def test_symmetric_difference_duplicate_elements():
    """Test symmetric difference with duplicate elements"""
    assert set(symmetric_difference([1, 2, 2, 3], [3, 4, 4, 5])) == {1, 2, 4, 5}

def test_symmetric_difference_invalid_input_type():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        symmetric_difference("not a list", [1, 2, 3])
    
    with pytest.raises(TypeError):
        symmetric_difference([1, 2, 3], "not a list")

def test_symmetric_difference_different_types():
    """Test symmetric difference with lists of different types"""
    assert set(symmetric_difference([1, 'a'], ['a', 2])) == {1, 2}