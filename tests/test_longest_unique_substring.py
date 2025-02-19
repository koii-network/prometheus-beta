import pytest
from src.longest_unique_substring import longest_unique_substring

def test_longest_unique_substring_examples():
    # Basic test cases from problem description
    assert longest_unique_substring("abcabcbb") == 3  # "abc"
    assert longest_unique_substring("bbbbb") == 1     # "b"
    assert longest_unique_substring("pwwkew") == 3    # "wke"

def test_longest_unique_substring_edge_cases():
    # Edge cases
    assert longest_unique_substring("") == 0          # Empty string
    assert longest_unique_substring("a") == 1         # Single character
    assert longest_unique_substring("au") == 2        # Two unique characters
    assert longest_unique_substring("dvdf") == 3      # Non-consecutive unique characters

def test_longest_unique_substring_complex_cases():
    # More complex scenarios
    assert longest_unique_substring("abcdefg") == 7   # All unique characters
    assert longest_unique_substring("aab") == 2       # Repeating character
    assert longest_unique_substring("tmmzuxt") == 5   # Tricky case with multiple unique substrings

def test_longest_unique_substring_unicode():
    # Unicode character support
    assert longest_unique_substring("नमस्ते") == 6  # Hindi word with no repeated characters
    assert longest_unique_substring("hello世界") == 7  # Mixed language characters

def test_longest_unique_substring_spaces_symbols():
    # Spaces and symbols
    assert longest_unique_substring("a b c") == 5   # Spaces as unique characters
    assert longest_unique_substring("!@#$%") == 5   # Symbol characters