import pytest
from src.longest_unique_substring import longest_unique_substring

def test_basic_scenarios():
    # Standard cases with repeating characters
    assert longest_unique_substring("abcabcbb") == 3  # Longest substring is "abc"
    assert longest_unique_substring("bbbbb") == 1     # Only one unique character
    assert longest_unique_substring("pwwkew") == 3    # Longest substring is "wke"

def test_edge_cases():
    # Empty string
    assert longest_unique_substring("") == 0
    
    # Single character
    assert longest_unique_substring("a") == 1
    assert longest_unique_substring("z") == 1

def test_complex_scenarios():
    # Complex scenarios with mixed characters
    assert longest_unique_substring("dvdf") == 3      # Handles edge case with multiple windows
    assert longest_unique_substring("tmmzuxt") == 5   # More complex repeated patterns
    
def test_all_unique_characters():
    # Strings with all unique characters
    assert longest_unique_substring("abcdefg") == 7
    assert longest_unique_substring("qwertyuiop") == 10

def test_unicode_characters():
    # Unicode and special character handling
    assert longest_unique_substring("こんにちは") == 6
    assert longest_unique_substring("Hello, World!") == 10

def test_case_sensitivity():
    # Case-sensitive scenarios
    assert longest_unique_substring("AbCdEfG") == 7
    assert longest_unique_substring("aAbBcC") == 2  # Different cases are different characters