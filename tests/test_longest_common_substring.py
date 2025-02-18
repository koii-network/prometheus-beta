import pytest
from src.longest_common_substring import find_longest_common_substring

def test_basic_common_substring():
    assert find_longest_common_substring("hello", "well") == "el"
    assert find_longest_common_substring("programming", "programmer") == "program"

def test_no_common_substring():
    assert find_longest_common_substring("abc", "xyz") == ""

def test_identical_strings():
    assert find_longest_common_substring("hello", "hello") == "hello"

def test_case_sensitive():
    assert find_longest_common_substring("Hello", "hello") == ""

def test_empty_strings():
    assert find_longest_common_substring("", "") == ""
    assert find_longest_common_substring("abc", "") == ""
    assert find_longest_common_substring("", "xyz") == ""

def test_multiple_common_substrings():
    assert find_longest_common_substring("abcdef", "bcdfgh") == "bcd"

def test_overlapping_common_substrings():
    assert find_longest_common_substring("ababab", "bab") == "bab"

def test_single_character_common_substring():
    assert find_longest_common_substring("abc", "cde") == "c"