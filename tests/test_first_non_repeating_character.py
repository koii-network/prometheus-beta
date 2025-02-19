import pytest
from src.first_non_repeating_character import first_non_repeating_character

def test_first_non_repeating_character():
    # Test cases with non-repeating characters
    assert first_non_repeating_character("hello") == 'h'
    assert first_non_repeating_character("aabbcdeeff") == 'c'
    assert first_non_repeating_character("abcabc") == None
    
    # Edge cases
    assert first_non_repeating_character("") == None
    assert first_non_repeating_character("a") == 'a'
    
    # Test with longer strings
    assert first_non_repeating_character("leetcode") == 'l'
    assert first_non_repeating_character("aaaaabccccddddeee") == 'b'
    
    # Ensure function works consistently with multiple calls
    result1 = first_non_repeating_character("stress")
    result2 = first_non_repeating_character("stress")
    assert result1 == result2 == 't'