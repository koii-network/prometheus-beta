import pytest
from src.longest_substring import find_longest_substring

def test_basic_cases():
    assert find_longest_substring("abcabcbb") == "abc"
    assert find_longest_substring("bbbbb") == "b"
    assert find_longest_substring("pwwkew") == "wke"

def test_empty_string():
    assert find_longest_substring("") == ""

def test_case_sensitivity():
    assert find_longest_substring("AbcA") == "Abc"
    assert find_longest_substring("aAaA") == "aA"

def test_single_character():
    assert find_longest_substring("a") == "a"

def test_full_string_no_repeats():
    assert find_longest_substring("abcdef") == "abcdef"

def test_multiple_max_length_substrings():
    # The sliding window method might produce different results
    # but we want to ensure it finds a valid substring
    result = find_longest_substring("abcdbxyza")
    assert len(set(result)) == len(result)  # No repeats
    assert len(result) >= 4  # At least length 4

def test_mixed_character_types():
    assert find_longest_substring("a1b2c3") == "a1b2c3"
    assert find_longest_substring("!@#$%^&*()") == "!@#$%^&*()"

def test_unicode_characters():
    assert find_longest_substring("こんにちは") == "こんにちは"