import pytest
from src.longest_common_substring import longest_common_substring

def test_basic_common_substring():
    assert longest_common_substring("ABCDGH", "ACDGHR") == "CDGH"

def test_no_common_substring():
    assert longest_common_substring("ABC", "XYZ") == ""

def test_identical_strings():
    assert longest_common_substring("hello", "hello") == "hello"

def test_partial_common_substring():
    assert longest_common_substring("programming", "programmer") == "programm"

def test_empty_inputs():
    assert longest_common_substring("", "test") == ""
    assert longest_common_substring("test", "") == ""
    assert longest_common_substring("", "") == ""

def test_case_sensitive():
    assert longest_common_substring("Hello", "hello") == ""

def test_substring_at_beginning():
    assert longest_common_substring("abcdef", "abcxyz") == "abc"

def test_substring_at_end():
    assert longest_common_substring("xyzabc", "123abc") == "abc"