import pytest
from src.longest_common_subsequence import longest_common_subsequence

def test_lcs_basic_cases():
    # Basic scenarios
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_lcs_edge_cases():
    # Edge cases
    assert longest_common_subsequence("", "ABC") == ""
    assert longest_common_subsequence("XYZ", "") == ""
    assert longest_common_subsequence("", "") == ""

def test_lcs_no_common_subsequence():
    # No common subsequence
    assert longest_common_subsequence("ABC", "XYZ") == ""

def test_lcs_identical_strings():
    # Identical strings
    assert longest_common_subsequence("HELLO", "HELLO") == "HELLO"

def test_lcs_partial_match():
    # Partial match
    assert longest_common_subsequence("ABCBDAB", "BDCABA") == "BCBA"

def test_lcs_repeated_characters():
    # Repeated characters
    assert longest_common_subsequence("AAAAAA", "AAAAAA") == "AAAAAA"
    assert longest_common_subsequence("ABCABC", "ABCABC") == "ABCABC"

def test_lcs_case_sensitivity():
    # Case sensitivity
    assert longest_common_subsequence("Hello", "hello") == ""