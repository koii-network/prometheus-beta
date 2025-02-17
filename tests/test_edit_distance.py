import pytest
from src.edit_distance import edit_distance

def test_edit_distance_same_strings():
    """Test when strings are identical"""
    assert edit_distance("hello", "hello") == 0

def test_edit_distance_empty_strings():
    """Test with empty strings"""
    assert edit_distance("", "") == 0
    assert edit_distance("hello", "") == 5
    assert edit_distance("", "world") == 5

def test_edit_distance_basic_transformations():
    """Test basic edit distance scenarios"""
    assert edit_distance("kitten", "sitting") == 3
    assert edit_distance("sunday", "saturday") == 3

def test_edit_distance_case_sensitive():
    """Test case sensitivity"""
    assert edit_distance("Hello", "hello") == 1

def test_edit_distance_error_handling():
    """Test error handling for None inputs"""
    with pytest.raises(ValueError):
        edit_distance(None, "test")
    with pytest.raises(ValueError):
        edit_distance("test", None)
    with pytest.raises(ValueError):
        edit_distance(None, None)

def test_edit_distance_unicode():
    """Test with Unicode characters"""
    assert edit_distance("café", "cafe") == 1
    assert edit_distance("résumé", "resume") == 2