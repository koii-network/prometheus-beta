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
    assert are_anagrams("Tea", "Eat") == True
    assert are_anagrams("Debit Card", "Bad Credit") == True

def test_whitespace_handling():
    """Test whitespace handling"""
    assert are_anagrams("rail safety", "fairy tales") == True
    assert are_anagrams("   stop   ", "posts") == True

def test_edge_cases():
    """Test edge cases"""
    assert are_anagrams("", "") == True  # Empty strings
    assert are_anagrams("a", "a") == True  # Single character
    assert are_anagrams("a", "b") == False  # Different single characters

def test_type_handling():
    """Test handling of incorrect input types"""
    with pytest.raises(TypeError):
        are_anagrams(123, "abc")
    with pytest.raises(TypeError):
        are_anagrams("abc", None)