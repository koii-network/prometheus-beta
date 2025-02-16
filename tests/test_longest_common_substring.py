import pytest
from src.longest_common_substring import find_longest_common_substring

def test_basic_common_substring():
    assert find_longest_common_substring("hello", "hello world") == "hello"
    assert find_longest_common_substring("programming", "program") == "program"

def test_no_common_substring():
    assert find_longest_common_substring("abc", "xyz") == ""

def test_empty_strings():
    assert find_longest_common_substring("", "test") == ""
    assert find_longest_common_substring("test", "") == ""
    assert find_longest_common_substring("", "") == ""

def test_case_sensitivity():
    assert find_longest_common_substring("Hello", "hello") == ""

def test_multiple_common_substrings():
    assert find_longest_common_substring("abcdef", "bcdefg") == "bcdef"

def test_identical_strings():
    assert find_longest_common_substring("python", "python") == "python"

def test_partial_common_substring():
    assert find_longest_common_substring("banana", "ananas") == "anan"