import pytest
from src.remove_duplicates import remove_duplicate_chars

def test_remove_duplicate_chars_basic():
    """Test basic duplicate removal"""
    assert remove_duplicate_chars("hello") == "helo"
    assert remove_duplicate_chars("aabbcc") == "abc"

def test_remove_duplicate_chars_preserve_order():
    """Test that original order is preserved"""
    assert remove_duplicate_chars("cabbage") == "cabge"

def test_remove_duplicate_chars_empty_string():
    """Test empty string"""
    assert remove_duplicate_chars("") == ""

def test_remove_duplicate_chars_no_duplicates():
    """Test string with no duplicates"""
    assert remove_duplicate_chars("python") == "python"

def test_remove_duplicate_chars_error_handling():
    """Test error handling for non-string inputs"""
    with pytest.raises(TypeError):
        remove_duplicate_chars(123)
    
    with pytest.raises(TypeError):
        remove_duplicate_chars(None)

def test_remove_duplicate_chars_mixed_case():
    """Test mixed case characters"""
    assert remove_duplicate_chars("HeLLo") == "HeLo"

def test_remove_duplicate_chars_special_characters():
    """Test with special characters and spaces"""
    assert remove_duplicate_chars("h e l l o !") == "h e lo!"