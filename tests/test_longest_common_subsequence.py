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
    assert longest_common_subsequence_length("Abc", "abc") == 1  # Only 'c' matches
    assert longest_common_subsequence_length("aB", "ab") == 0
    assert longest_common_subsequence_length("aA", "aa") == 1

def test_repeated_characters():
    assert longest_common_subsequence_length("aaa", "aa") == 2
    assert longest_common_subsequence_length("aabb", "ab") == 2

def test_case_sensitivity_detailed():
    # Ensuring exact character match with proper index
    test_cases = [
        ("Abc", "abc", 1),  # Only 'c' matches
        ("aB", "ab", 0),    # No match
        ("abC", "abc", 2),  # Matches 'ab'
        ("Cab", "cab", 2),  # Matches 'ab'
    ]
    
    for str1, str2, expected_length in test_cases:
        assert longest_common_subsequence_length(str1, str2) == expected_length, \
            f"Failed for strings {str1} and {str2}"