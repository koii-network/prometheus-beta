import pytest
from src.longest_substring import find_longest_substring

def test_find_longest_substring():
    # Test various scenarios
    assert find_longest_substring("") == ""
    assert find_longest_substring("abcabcbb") == "abc"
    assert find_longest_substring("bbbbb") == "b"
    assert find_longest_substring("pwwkew") == "wke"
    
    # Case-sensitive tests
    assert find_longest_substring("ABCabcABC") == "ABCabc"
    assert find_longest_substring("AAbbCC") == "Bb"
    
    # Edge cases
    assert find_longest_substring("a") == "a"
    assert find_longest_substring("aA") == "aA"
    
    # Complex case with longer non-repeating substring
    assert find_longest_substring("dvdf") == "vdf"
    
def test_edge_cases():
    # Additional edge cases
    assert find_longest_substring(" ") == " "
    assert find_longest_substring("!!@#") == "!@#"
    
def test_case_sensitivity():
    # Ensuring case sensitivity
    assert find_longest_substring("aA") != "a"
    assert find_longest_substring("AbCdEfG") == "AbCdEfG"