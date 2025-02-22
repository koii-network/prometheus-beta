import pytest
from src.sequence_reconstruction import min_sequence_edits

def test_identical_sequences():
    """Test when sequences are identical"""
    original = [1, 2, 3, 4, 5]
    modified = [1, 2, 3, 4, 5]
    assert min_sequence_edits(original, modified) == 0

def test_completely_different_sequences():
    """Test when sequences have no common elements"""
    original = [1, 2, 3]
    modified = [4, 5, 6]
    assert min_sequence_edits(original, modified) == 6

def test_partial_match():
    """Test a scenario with partial matching elements"""
    original = [1, 2, 3, 4, 5]
    modified = [1, 3, 5]
    assert min_sequence_edits(original, modified) == 2

def test_sequence_with_insertions():
    """Test a scenario with additional elements in modified sequence"""
    original = [1, 2, 3]
    modified = [1, 2, 3, 4, 5]
    assert min_sequence_edits(original, modified) == 2

def test_sequence_with_removals():
    """Test a scenario with elements removed from modified sequence"""
    original = [1, 2, 3, 4, 5]
    modified = [2, 4]
    assert min_sequence_edits(original, modified) == 3

def test_empty_sequences():
    """Test behavior with empty sequences"""
    original = []
    modified = [1, 2, 3]
    assert min_sequence_edits(original, modified) == 3

def test_mixed_edits():
    """Test a scenario with both insertions and removals"""
    original = [1, 2, 3, 4, 5]
    modified = [2, 4, 6, 7]
    assert min_sequence_edits(original, modified) == 4