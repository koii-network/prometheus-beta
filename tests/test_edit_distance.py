import pytest
from src.edit_distance import compute_edit_distance

def test_identical_strings():
    """Test edit distance for identical strings"""
    assert compute_edit_distance("hello", "hello") == 0

def test_empty_strings():
    """Test edit distance with empty strings"""
    assert compute_edit_distance("", "") == 0
    assert compute_edit_distance("hello", "") == 5
    assert compute_edit_distance("", "world") == 5

def test_simple_edits():
    """Test basic edit scenarios"""
    # Insertions
    assert compute_edit_distance("cat", "cats") == 1
    
    # Deletions
    assert compute_edit_distance("hello", "hell") == 1
    
    # Substitutions
    assert compute_edit_distance("kitten", "sitting") == 3

def test_complex_transformations():
    """Test more complex string transformations"""
    assert compute_edit_distance("sunday", "saturday") == 3
    assert compute_edit_distance("horse", "ros") == 3

def test_case_sensitivity():
    """Test case-sensitive edit distance"""
    assert compute_edit_distance("Hello", "hello") == 1
    assert compute_edit_distance("Coding", "coding") == 1

def test_invalid_inputs():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        compute_edit_distance(123, "hello")
    
    with pytest.raises(TypeError):
        compute_edit_distance("hello", None)

def test_unicode_strings():
    """Test edit distance with unicode characters"""
    assert compute_edit_distance("café", "cafe") == 1
    assert compute_edit_distance("こんにちは", "こんばんは") == 2