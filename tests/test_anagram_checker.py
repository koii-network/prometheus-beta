import pytest
from src.anagram_checker import are_anagrams

def test_basic_anagrams():
    """Test basic anagram scenarios"""
    assert are_anagrams('listen', 'silent') == True
    assert are_anagrams('hello', 'world') == False

def test_case_insensitive():
    """Test that the function is case-insensitive"""
    assert are_anagrams('Tea', 'Eat') == True
    assert are_anagrams('Race', 'Care') == True

def test_whitespace_handling():
    """Test anagram detection with whitespace"""
    assert are_anagrams('debit card', 'bad credit') == True
    assert are_anagrams('  hello', 'hello  ') == True

def test_empty_strings():
    """Test handling of empty strings"""
    assert are_anagrams('', '') == True
    assert are_anagrams('a', '') == False

def test_unicode_characters():
    """Test anagram detection with unicode characters"""
    assert are_anagrams('résumé', 'émusér') == True

def test_type_error():
    """Test that TypeError is raised for non-string inputs"""
    with pytest.raises(TypeError):
        are_anagrams(123, 'abc')
    with pytest.raises(TypeError):
        are_anagrams('abc', None)
    with pytest.raises(TypeError):
        are_anagrams([], {})