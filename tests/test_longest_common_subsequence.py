import pytest
from src.longest_common_subsequence import find_longest_common_subsequence

def test_normal_case():
    assert find_longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert find_longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_empty_strings():
    assert find_longest_common_subsequence("", "") == ""
    assert find_longest_common_subsequence("hello", "") == ""
    assert find_longest_common_subsequence("", "world") == ""

def test_identical_strings():
    assert find_longest_common_subsequence("hello", "hello") == "hello"

def test_no_common_subsequence():
    assert find_longest_common_subsequence("abc", "xyz") == ""

def test_partial_matches():
    assert find_longest_common_subsequence("abcde", "ace") == "ace"

def test_invalid_input_types():
    with pytest.raises(TypeError):
        find_longest_common_subsequence(123, "hello")
    with pytest.raises(TypeError):
        find_longest_common_subsequence("hello", None)
    with pytest.raises(TypeError):
        find_longest_common_subsequence(None, None)