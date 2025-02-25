import pytest
from src.count_anagrams import count_anagrams

def test_count_anagrams_basic():
    """Test basic anagram counting scenarios."""
    assert count_anagrams('abab') == 2
    assert count_anagrams('abcde') == 0
    assert count_anagrams('aabb') == 3

def test_count_anagrams_edge_cases():
    """Test edge cases and boundary conditions."""
    assert count_anagrams('') == 0
    assert count_anagrams('a') == 0
    assert count_anagrams('aa') == 1

def test_count_anagrams_longer_string():
    """Test anagram counting in longer strings."""
    assert count_anagrams('abcabcabc') > 0

def test_count_anagrams_invalid_input():
    """Test that invalid inputs raise a ValueError."""
    with pytest.raises(ValueError):
        count_anagrams('AbCd')  # Mixed case
    
    with pytest.raises(ValueError):
        count_anagrams('ab1c')  # Non-letter characters

def test_count_anagrams_repeated_chars():
    """Test strings with repeated characters."""
    assert count_anagrams('aaaa') == 1