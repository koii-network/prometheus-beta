import pytest
from src.longest_common_subsequence import find_longest_common_subsequence

def test_basic_lcs():
    # Basic cases with common subsequence
    assert find_longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert find_longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_identical_strings():
    # When strings are identical
    assert find_longest_common_subsequence("hello", "hello") == "hello"

def test_no_common_subsequence():
    # When no common subsequence exists
    assert find_longest_common_subsequence("abc", "xyz") == ""

def test_empty_strings():
    # Test with empty strings
    assert find_longest_common_subsequence("", "") == ""
    assert find_longest_common_subsequence("hello", "") == ""
    assert find_longest_common_subsequence("", "world") == ""

def test_one_character_match():
    # Test when only one character matches
    assert find_longest_common_subsequence("a", "a") == "a"
    assert find_longest_common_subsequence("abc", "cde") == "c"

def test_type_error():
    # Test type checking
    with pytest.raises(TypeError):
        find_longest_common_subsequence(123, "hello")
    with pytest.raises(TypeError):
        find_longest_common_subsequence("hello", ["world"])
    with pytest.raises(TypeError):
        find_longest_common_subsequence(None, None)

def test_case_sensitivity():
    # Test case sensitivity
    assert find_longest_common_subsequence("Hello", "hello") == ""