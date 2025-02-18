import pytest
from src.longest_common_substring import longest_common_substring

def test_basic_common_substring():
    assert longest_common_substring("hello", "world") == "l"
    assert longest_common_substring("programming", "programmer") == "program"

def test_no_common_substring():
    assert longest_common_substring("abc", "xyz") == ""

def test_identical_strings():
    assert longest_common_substring("python", "python") == "python"

def test_empty_strings():
    assert longest_common_substring("", "") == ""
    assert longest_common_substring("abc", "") == ""
    assert longest_common_substring("", "def") == ""

def test_multiple_substring_options():
    assert longest_common_substring("abcdef", "bcdefg") == "bcdef"

def test_case_sensitivity():
    assert longest_common_substring("Hello", "hello") == ""

def test_long_strings():
    str1 = "This is a longer test string with multiple potential substrings"
    str2 = "Another long test string with potential matches"
    assert len(longest_common_substring(str1, str2)) > 0

def test_substring_at_start_or_end():
    assert longest_common_substring("startsame", "samestarts") == "same"