import pytest
from src.anagram_counter import count_anagrams

def test_basic_anagram_counting():
    # Basic test cases with known results
    assert count_anagrams('aab') == 3  # 'a', 'a', 'b' have unique sorted signatures
    assert count_anagrams('abcde') == 5  # Each unique letter is a distinct anagram
    assert count_anagrams('aaaa') == 1  # All are the same, so only one signature

def test_longer_string_anagrams():
    # More complex string with multiple anagram signatures
    result = count_anagrams('abba')
    assert result == 4  # Includes 'a', 'b', 'ab', 'ba'

def test_single_character():
    # Single character should always return 1
    assert count_anagrams('z') == 1

def test_error_handling():
    # Test invalid inputs
    with pytest.raises(ValueError, match="Input must be a non-empty string of lowercase letters"):
        count_anagrams('')
    
    with pytest.raises(ValueError, match="Input must be a non-empty string of lowercase letters"):
        count_anagrams('ABC')  # Uppercase letters
    
    with pytest.raises(ValueError, match="Input must be a non-empty string of lowercase letters"):
        count_anagrams('a1b')  # Contains non-letter character

def test_edge_cases():
    # More edge case tests to ensure comprehensive coverage
    assert count_anagrams('aaa') == 1
    assert count_anagrams('abcabc') == 6