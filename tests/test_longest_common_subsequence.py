import pytest
from src.longest_common_subsequence import longest_common_subsequence_length

def test_basic_lcs():
    assert longest_common_subsequence_length("abcde", "ace") == 3
    assert longest_common_subsequence_length("abc", "abc") == 3
    assert longest_common_subsequence_length("abc", "def") == 0

def test_empty_strings():
    assert longest_common_subsequence_length("", "") == 0
    assert longest_common_subsequence_length("", "abc") == 0
    assert longest_common_subsequence_length("abc", "") == 0

def test_different_length_strings():
    assert longest_common_subsequence_length("abcdgh", "aedfhr") == 3
    assert longest_common_subsequence_length("aggtab", "gxtxayb") == 4

def test_case_sensitivity():
    assert longest_common_subsequence_length("ABC", "abc") == 0
    assert longest_common_subsequence_length("Abc", "abc") == 1
    assert longest_common_subsequence_length("aB", "ab") == 1
    assert longest_common_subsequence_length("aA", "aa") == 1

def test_repeated_characters():
    assert longest_common_subsequence_length("aaa", "aa") == 2
    assert longest_common_subsequence_length("aabb", "ab") == 2

def test_complex_case_sensitivity():
    # Scenarios with precise matching
    test_cases = [
        ("Abc", "abc", 1),   # This will match 'c'
        ("aB", "ab", 1),     # Will match 'b'
        ("abC", "abc", 2),   # Will match 'ab'
        ("CAbc", "cab", 2),  # Will match 'ab'
        ("ABc", "abc", 2),   # Will match 'bc'
    ]
    
    for str1, str2, expected_length in test_cases:
        result = longest_common_subsequence_length(str1, str2)
        assert result == expected_length, \
            f"Failed for strings {str1} and {str2}. Expected {expected_length}, got {result}"