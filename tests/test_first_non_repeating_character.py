import pytest
from src.first_non_repeating_character import first_non_repeating_character

def test_first_non_repeating_character():
    # Test case with a non-repeating character
    assert first_non_repeating_character("leetcode") == "l"
    
    # Test case with repeating characters, but one non-repeating
    assert first_non_repeating_character("loveleetcode") == "v"
    
    # Test case with all repeating characters
    assert first_non_repeating_character("aabb") == None
    
    # Test case with single character
    assert first_non_repeating_character("a") == "a"
    
    # Test case with empty string
    assert first_non_repeating_character("") == None
    
    # Test case with many characters and a non-repeating character near end
    assert first_non_repeating_character("aabcccdeeff") == "b"
    
    # Test case with all same characters
    assert first_non_repeating_character("zzzzz") == None