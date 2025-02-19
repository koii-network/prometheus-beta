import pytest
from src.string_transform import string_transform

def test_string_transform_basic():
    """Test basic string transformation"""
    assert string_transform("Hello World") == "dlrow*lleo"

def test_string_transform_mixed_case():
    """Test transformation with mixed case letters"""
    assert string_transform("Hello WORLD") == "dlrow*lleo"

def test_string_transform_with_spaces():
    """Test transformation with multiple spaces"""
    assert string_transform("  Hello   World  ") == "dlrow*lleo"

def test_string_transform_no_changes():
    """Test transformation with no original 'a' letters"""
    assert string_transform("Python") == "nohtyp"

def test_string_transform_multiple_a_letters():
    """Test transformation with multiple 'a' letters"""
    assert string_transform("banana") == "*n*n*b"

def test_string_transform_empty_string():
    """Test transformation of an empty string"""
    assert string_transform("") == ""

def test_string_transform_special_characters():
    """Test transformation with special characters"""
    assert string_transform("Hello, World! 123") == "321dlrow*lleo"