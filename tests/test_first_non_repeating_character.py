import pytest
from src.first_non_repeating_character import first_non_repeating_character

def test_first_non_repeating_character():
    # Test cases with single non-repeating character
    assert first_non_repeating_character("leetcode") == "l"
    assert first_non_repeating_character("loveleetcode") == "v"
    
    # Test case with no non-repeating characters
    assert first_non_repeating_character("aabb") == None
    
    # Test case with all unique characters
    assert first_non_repeating_character("abcde") == "a"
    
    # Test case with empty string
    assert first_non_repeating_character("") == None
    
    # Test single character string
    assert first_non_repeating_character("a") == "a"
    assert first_non_repeating_character("z") == "z"
    
    # Edge cases
    assert first_non_repeating_character("zzzzaaaaabbbbb") == None