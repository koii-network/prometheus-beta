import pytest
from src.edit_distance import edit_distance

def test_same_strings():
    """Test when both strings are identical"""
    assert edit_distance("hello", "hello") == 0

def test_empty_strings():
    """Test with empty strings"""
    assert edit_distance("", "") == 0
    assert edit_distance("hello", "") == 5
    assert edit_distance("", "world") == 5

def test_different_length_strings():
    """Test strings of different lengths"""
    assert edit_distance("cat", "cats") == 1  # one insertion
    assert edit_distance("kitten", "sitting") == 3  # multiple edits

def test_full_transformation():
    """Test complete string transformations"""
    assert edit_distance("saturday", "sunday") == 3

def test_case_sensitivity():
    """Verify that function is case-sensitive"""
    assert edit_distance("Hello", "hello") == 1

def test_type_error():
    """Ensure type checking works"""
    with pytest.raises(TypeError):
        edit_distance(123, "hello")
    with pytest.raises(TypeError):
        edit_distance("hello", None)

def test_complex_edits():
    """Test more complex edit scenarios"""
    assert edit_distance("pale", "ple") == 1  # deletion
    assert edit_distance("pales", "pale") == 1  # deletion
    assert edit_distance("pale", "bale") == 1  # substitution
    assert edit_distance("pale", "bake") == 2  # two substitutions

def test_unicode_strings():
    """Test with unicode characters"""
    assert edit_distance("café", "cafe") == 1  # accent substitution
    assert edit_distance("こんにちは", "こんばんは") == 1  # Japanese characters