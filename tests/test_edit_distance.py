import pytest
from src.edit_distance import compute_edit_distance

def test_same_strings():
    """Test strings that are exactly the same"""
    assert compute_edit_distance("hello", "hello") == 0

def test_empty_strings():
    """Test empty strings"""
    assert compute_edit_distance("", "") == 0
    assert compute_edit_distance("hello", "") == 5
    assert compute_edit_distance("", "world") == 5

def test_insertion():
    """Test cases requiring insertions"""
    assert compute_edit_distance("cat", "chat") == 1
    assert compute_edit_distance("", "hello") == 5

def test_deletion():
    """Test cases requiring deletions"""
    assert compute_edit_distance("hello", "helo") == 1
    assert compute_edit_distance("hello", "") == 5

def test_substitution():
    """Test cases requiring substitutions"""
    assert compute_edit_distance("kitten", "sitting") == 3
    assert compute_edit_distance("hello", "hallo") == 1

def test_complex_transformations():
    """Test more complex string transformations"""
    assert compute_edit_distance("saturday", "sunday") == 3
    assert compute_edit_distance("rosettacode", "roseanna") == 4

def test_case_sensitivity():
    """Test case-sensitive comparisons"""
    assert compute_edit_distance("Hello", "hello") == 1

def test_invalid_input():
    """Test handling of None inputs"""
    with pytest.raises(ValueError):
        compute_edit_distance(None, "hello")
    with pytest.raises(ValueError):
        compute_edit_distance("hello", None)
    with pytest.raises(ValueError):
        compute_edit_distance(None, None)