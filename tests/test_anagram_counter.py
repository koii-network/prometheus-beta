import pytest
from src.anagram_counter import count_anagrams

def test_basic_anagram_count():
    """Test basic anagram counting scenarios."""
    assert count_anagrams('abab') == 3
    assert count_anagrams('aa') == 1
    assert count_anagrams('abc') == 6

def test_single_character_string():
    """Test single character input."""
    assert count_anagrams('a') == 1

def test_repeated_characters():
    """Test strings with repeated characters."""
    assert count_anagrams('aaaa') == 1
    assert count_anagrams('aabb') == 3

def test_invalid_input():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be a non-empty string with only lowercase letters"):
        count_anagrams('')
    
    with pytest.raises(ValueError, match="Input must be a non-empty string with only lowercase letters"):
        count_anagrams('AbC')
    
    with pytest.raises(ValueError, match="Input must be a non-empty string with only lowercase letters"):
        count_anagrams('123')

def test_longer_string():
    """Test a longer input string."""
    assert count_anagrams('abcde') == 15