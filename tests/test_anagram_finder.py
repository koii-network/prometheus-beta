import pytest
from src.anagram_finder import find_anagrams

def test_find_anagrams_basic():
    """Test basic anagram finding functionality."""
    word_list = ['listen', 'silent', 'enlist', 'hello', 'world']
    result = find_anagrams('listen', word_list)
    assert set(result) == {'silent', 'enlist'}

def test_find_anagrams_case_insensitive():
    """Test that anagram finding is case-insensitive."""
    word_list = ['Race', 'Care', 'Acre', 'Face']
    result = find_anagrams('race', word_list)
    assert set(result) == {'care', 'acre'}

def test_find_anagrams_no_anagrams():
    """Test behavior when no anagrams are found."""
    word_list = ['hello', 'world', 'python']
    result = find_anagrams('test', word_list)
    assert result == []

def test_find_anagrams_empty_list():
    """Test behavior with an empty word list."""
    result = find_anagrams('test', [])
    assert result == []

def test_find_anagrams_invalid_word():
    """Test error handling for invalid word input."""
    with pytest.raises(ValueError, match="Input word must be a string"):
        find_anagrams(123, ['test', 'best'])

def test_find_anagrams_invalid_word_list():
    """Test error handling for invalid word list input."""
    with pytest.raises(ValueError, match="Word list must be a list"):
        find_anagrams('test', 'not a list')

def test_find_anagrams_exclude_original():
    """Test that the original word is not returned as its own anagram."""
    word_list = ['listen', 'silent', 'listen']
    result = find_anagrams('listen', word_list)
    assert result == ['silent']