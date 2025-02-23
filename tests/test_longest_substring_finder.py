import pytest
from src.longest_substring_finder import find_longest_substring

def test_typical_cases():
    assert find_longest_substring("abcabcbb") == "abc"
    assert find_longest_substring("bbbbb") == "b"
    assert find_longest_substring("pwwkew") == "wke"

def test_empty_string():
    assert find_longest_substring("") == ""

def test_single_character():
    assert find_longest_substring("a") == "a"

def test_case_sensitivity():
    assert find_longest_substring("AbcA") == "Abc"
    assert find_longest_substring("aA") == "aA"

def test_all_unique_characters():
    assert find_longest_substring("abcdef") == "abcdef"

def test_repeated_characters_start():
    assert find_longest_substring("aabcdef") == "abcdef"

def test_repeated_characters_middle():
    assert find_longest_substring("abcadef") == "bcadef"

def test_unicode_characters():
    assert find_longest_substring("こんにちは") == "こんにちは"

def test_mixed_unicode_and_ascii():
    assert find_longest_substring("hello世界") == "lo世界"

def test_long_string_with_repeats():
    long_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" * 2
    longest = find_longest_substring(long_string)
    assert len(longest) == 62  # unique characters in the string
    assert len(set(longest)) == 62  # ensure no repeats