import pytest
from src.longest_common_subsequence import find_longest_common_subsequence

def test_basic_lcs():
    assert find_longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert find_longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_identical_strings():
    assert find_longest_common_subsequence("hello", "hello") == "hello"

def test_no_common_subsequence():
    assert find_longest_common_subsequence("abc", "xyz") == ""

def test_one_empty_string():
    assert find_longest_common_subsequence("", "hello") == ""
    assert find_longest_common_subsequence("world", "") == ""

def test_both_empty_strings():
    assert find_longest_common_subsequence("", "") == ""

def test_partial_common_subsequence():
    assert find_longest_common_subsequence("ABCBDAB", "BDCABA") == "BCBA"

def test_case_sensitivity():
    assert find_longest_common_subsequence("Hello", "hello") == ""

def test_type_error():
    with pytest.raises(TypeError):
        find_longest_common_subsequence(123, "hello")
    with pytest.raises(TypeError):
        find_longest_common_subsequence("hello", [1, 2, 3])
    with pytest.raises(TypeError):
        find_longest_common_subsequence(None, "hello")