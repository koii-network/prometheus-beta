import pytest
from src.anagram_counter import count_anagrams

def test_count_anagrams_basic():
    """Test basic anagram counting functionality."""
    assert count_anagrams('abab') == 3  # unique sorted substrings: 'a', 'ab', 'b'
    assert count_anagrams('abc') == 6   # unique sorted substrings: 'a', 'ab', 'abc', 'b', 'bc', 'c'

def test_count_anagrams_edge_cases():
    """Test edge cases of anagram counting."""
    assert count_anagrams('') == 0      # Empty string
    assert count_anagrams('a') == 0     # Single character
    assert count_anagrams('aa') == 1    # Repeated characters

def test_count_anagrams_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be a string"):
        count_anagrams(123)
    
    with pytest.raises(ValueError, match="Input must contain only lowercase English letters"):
        count_anagrams('ABC')
    
    with pytest.raises(ValueError, match="Input must contain only lowercase English letters"):
        count_anagrams('ab1c')

def test_count_anagrams_complex():
    """Test more complex anagram counting scenarios."""
    assert count_anagrams('aab') == 3   # 'a', 'aa', 'ab'
    assert count_anagrams('abcde') == 35  # Large number of unique sorted substrings