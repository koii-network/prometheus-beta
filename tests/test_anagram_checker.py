import pytest
from src.anagram_checker import anagram_checker

def test_basic_anagrams():
    """Test basic anagram scenarios"""
    assert anagram_checker('listen', 'silent') == True
    assert anagram_checker('hello', 'world') == False

def test_case_insensitive():
    """Test that anagram check is case-insensitive"""
    assert anagram_checker('Debit Card', 'Bad Credit') == True
    assert anagram_checker('Python', 'Typhon') == True

def test_whitespace_handling():
    """Test handling of whitespace in inputs"""
    assert anagram_checker('rail safety', 'fairy tales') == True
    assert anagram_checker(' rail safety ', 'fairy tales') == True

def test_empty_strings():
    """Test empty string scenarios"""
    assert anagram_checker('', '') == True

def test_different_lengths():
    """Test words of different lengths"""
    assert anagram_checker('short', 'shorter') == False
    assert anagram_checker('a', 'ab') == False

def test_invalid_inputs():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        anagram_checker(123, 'test')
    with pytest.raises(TypeError):
        anagram_checker('test', None)
    with pytest.raises(TypeError):
        anagram_checker([], {})