import pytest
from src.edit_distance import compute_edit_distance

def test_same_strings():
    """Test when both strings are identical"""
    assert compute_edit_distance("hello", "hello") == 0

def test_empty_strings():
    """Test with empty strings"""
    assert compute_edit_distance("", "") == 0
    assert compute_edit_distance("hello", "") == 5
    assert compute_edit_distance("", "world") == 5

def test_basic_edits():
    """Test basic edit scenarios"""
    # Insertion
    assert compute_edit_distance("cat", "chat") == 1
    
    # Deletion
    assert compute_edit_distance("hello", "helo") == 1
    
    # Substitution
    assert compute_edit_distance("kitten", "sitting") == 3

def test_complex_edits():
    """Test more complex edit scenarios"""
    assert compute_edit_distance("sunday", "saturday") == 3
    assert compute_edit_distance("saturday", "sunday") == 3
    assert compute_edit_distance("algorithm", "logarithm") == 3

def test_type_error():
    """Test type error handling"""
    with pytest.raises(TypeError):
        compute_edit_distance(123, "hello")
    
    with pytest.raises(TypeError):
        compute_edit_distance("hello", None)
    
    with pytest.raises(TypeError):
        compute_edit_distance([], "test")

def test_unicode_strings():
    """Test edit distance with Unicode strings"""
    assert compute_edit_distance("café", "cafe") == 1
    assert compute_edit_distance("naïve", "naive") == 1

def test_case_sensitivity():
    """Test edit distance is case-sensitive"""
    assert compute_edit_distance("Hello", "hello") == 1