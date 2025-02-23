import pytest
from src.anagram_checker import are_anagrams

def test_basic_anagrams():
    """Test basic anagram scenarios"""
    assert are_anagrams("listen", "silent") == True
    assert are_anagrams("triangle", "integral") == True

def test_case_insensitive():
    """Test that the function is case-insensitive"""
    assert are_anagrams("Tea", "Eat") == True
    assert are_anagrams("LISTEN", "silent") == True

def test_whitespace_handling():
    """Test handling of whitespace"""
    assert are_anagrams("debit card", "bad credit") == True
    assert are_anagrams("   hello   ", "olleh") == True

def test_non_anagrams():
    """Test strings that are not anagrams"""
    assert are_anagrams("hello", "world") == False
    assert are_anagrams("python", "java") == False

def test_empty_strings():
    """Test empty string scenarios"""
    assert are_anagrams("", "") == True

def test_same_string():
    """Test a string with itself"""
    assert are_anagrams("hello", "hello") == True

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        are_anagrams(123, "hello")
    with pytest.raises(TypeError):
        are_anagrams("hello", None)
    with pytest.raises(TypeError):
        are_anagrams([], "hello")

def test_different_lengths():
    """Test strings of different lengths"""
    assert are_anagrams("abc", "abcd") == False
    assert are_anagrams("a", "aa") == False