import pytest
from src.anagram_checker import are_anagrams

def test_basic_anagrams():
    """Test basic anagram scenarios"""
    assert are_anagrams("listen", "silent") == True
    assert are_anagrams("triangle", "integral") == True

def test_non_anagrams():
    """Test non-anagram scenarios"""
    assert are_anagrams("hello", "world") == False
    assert are_anagrams("python", "java") == False

def test_case_insensitive():
    """Test case-insensitive comparison"""
    assert are_anagrams("Listen", "Silent") == True
    assert are_anagrams("Tea", "Eat") == True

def test_whitespace_handling():
    """Test handling of whitespace"""
    assert are_anagrams("debit card", "bad credit") == True
    assert are_anagrams("  race", "care  ") == True

def test_empty_strings():
    """Test empty string scenarios"""
    assert are_anagrams("", "") == True

def test_different_lengths():
    """Test strings of different lengths"""
    assert are_anagrams("short", "longer") == False

def test_type_errors():
    """Test type validation"""
    with pytest.raises(TypeError):
        are_anagrams(123, "test")
    with pytest.raises(TypeError):
        are_anagrams("test", None)
    with pytest.raises(TypeError):
        are_anagrams([], "test")