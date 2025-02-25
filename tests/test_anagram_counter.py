import pytest
from src.anagram_counter import count_anagrams

def test_count_anagrams_basic():
    """Test basic anagram counting."""
    assert count_anagrams('abcde') == 15  # All unique sorted substrings

def test_count_anagrams_repeated_chars():
    """Test anagram counting with repeated characters."""
    assert count_anagrams('aaa') == 1  # Only one unique anagram signature

def test_count_anagrams_single_char():
    """Test anagram counting with a single character."""
    assert count_anagrams('a') == 1

def test_count_anagrams_short_string():
    """Test anagram counting with a short string."""
    assert count_anagrams('abc') == 6

def test_count_anagrams_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be a non-empty string of lowercase English letters"):
        count_anagrams('')
    
    with pytest.raises(ValueError, match="Input must be a non-empty string of lowercase English letters"):
        count_anagrams('ABC')
    
    with pytest.raises(ValueError, match="Input must be a non-empty string of lowercase English letters"):
        count_anagrams('ab1c')