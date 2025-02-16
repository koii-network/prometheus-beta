import pytest
from src.longest_common_substring import find_longest_common_substring

def test_basic_common_substring():
    assert find_longest_common_substring("hello", "world") == ""
    assert find_longest_common_substring("banana", "ananas") == "anas"
    assert find_longest_common_substring("programming", "programmer") == "program"

def test_edge_cases():
    assert find_longest_common_substring("", "") == ""
    assert find_longest_common_substring("abc", "") == ""
    assert find_longest_common_substring("", "xyz") == ""

def test_identical_strings():
    assert find_longest_common_substring("hello", "hello") == "hello"

def test_case_sensitivity():
    assert find_longest_common_substring("Hello", "hello") == ""

def test_long_substrings():
    str1 = "abcdefghijklmnop"
    str2 = "xyzabcdefghijklm"
    assert find_longest_common_substring(str1, str2) == "abcdefghijklm"

def test_invalid_input_types():
    with pytest.raises(TypeError):
        find_longest_common_substring(123, "abc")
    with pytest.raises(TypeError):
        find_longest_common_substring("abc", [1, 2, 3])
    with pytest.raises(TypeError):
        find_longest_common_substring(None, "test")