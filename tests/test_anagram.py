import pytest
from src.anagram import is_anagram

def test_simple_anagrams():
    """Test basic anagram scenarios"""
    assert is_anagram("listen", "silent") == True
    assert is_anagram("hello", "olleh") == True

def test_case_insensitive():
    """Test that anagram check is case-insensitive"""
    assert is_anagram("Tea", "Eat") == True
    assert is_anagram("RACE", "care") == True

def test_whitespace_handling():
    """Test that whitespace is ignored in anagram check"""
    assert is_anagram("debit card", "bad credit") == True
    assert is_anagram("a gentleman", "elegant man") == True

def test_non_anagrams():
    """Test that non-anagrams return False"""
    assert is_anagram("hello", "world") == False
    assert is_anagram("python", "java") == False

def test_empty_strings():
    """Test empty string scenarios"""
    assert is_anagram("", "") == True

def test_type_error():
    """Test that non-string inputs raise TypeError"""
    with pytest.raises(TypeError):
        is_anagram(123, "test")
    with pytest.raises(TypeError):
        is_anagram("test", None)

def test_unicode_support():
    """Test support for unicode characters"""
    assert is_anagram("café", "acéf") == True