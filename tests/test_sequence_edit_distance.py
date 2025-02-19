import pytest
from src.sequence_edit_distance import min_sequence_edit_distance

def test_identical_sequences():
    """Test when sequences are identical"""
    original = [1, 2, 3, 4]
    target = [1, 2, 3, 4]
    assert min_sequence_edit_distance(original, target) == 0

def test_completely_different_sequences():
    """Test when sequences have no common elements"""
    original = [1, 2, 3]
    target = [4, 5, 6]
    assert min_sequence_edit_distance(original, target) == 6

def test_partial_overlap():
    """Test sequences with partial overlap"""
    original = [1, 2, 3, 4, 5]
    target = [2, 4, 6]
    assert min_sequence_edit_distance(original, target) == 4

def test_empty_sequences():
    """Test when one or both sequences are empty"""
    original = []
    target = [1, 2, 3]
    assert min_sequence_edit_distance(original, target) == 3
    
    original = [1, 2, 3]
    target = []
    assert min_sequence_edit_distance(original, target) == 3

def test_single_element_sequences():
    """Test sequences with single elements"""
    original = [1]
    target = [2]
    assert min_sequence_edit_distance(original, target) == 2

def test_repeated_elements():
    """Test sequences with repeated elements"""
    original = [1, 1, 2, 2, 3]
    target = [1, 2, 3]
    assert min_sequence_edit_distance(original, target) == 2