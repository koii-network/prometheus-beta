import pytest
from src.longest_common_subsequence import longest_common_subsequence_length

def test_lcs_normal_cases():
    # Standard cases with common subsequences
    assert longest_common_subsequence_length("ABCDGH", "AEDFHR") == 3  # ADH
    assert longest_common_subsequence_length("AGGTAB", "GXTXAYB") == 4  # GTAB
    assert longest_common_subsequence_length("hello", "hello") == 5  # Identical strings

def test_lcs_edge_cases():
    # Empty string cases
    assert longest_common_subsequence_length("", "test") == 0
    assert longest_common_subsequence_length("test", "") == 0
    assert longest_common_subsequence_length("", "") == 0

def test_lcs_no_common_subsequence():
    # Strings with no common characters
    assert longest_common_subsequence_length("abc", "xyz") == 0
    assert longest_common_subsequence_length("python", "java") == 0

def test_lcs_partial_match():
    # Partial matching cases
    assert longest_common_subsequence_length("stone", "longest") == 3  # one
    assert longest_common_subsequence_length("programming", "ogram") == 5  # ogram

def test_lcs_case_sensitive():
    # Case-sensitive comparison
    assert longest_common_subsequence_length("Hello", "hello") == 0
    assert longest_common_subsequence_length("ABCD", "abcd") == 0