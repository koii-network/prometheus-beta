import pytest
from src.longest_common_subsequence import longest_common_subsequence

def test_basic_cases():
    # Basic cases with common subsequence
    assert longest_common_subsequence("ABCDGH", "AEDFHR") == "ADH"
    assert longest_common_subsequence("AGGTAB", "GXTXAYB") == "GTAB"

def test_edge_cases():
    # Empty string cases
    assert longest_common_subsequence("", "ABC") == ""
    assert longest_common_subsequence("XYZ", "") == ""
    assert longest_common_subsequence("", "") == ""

def test_no_common_subsequence():
    # Strings with no common subsequence
    assert longest_common_subsequence("ABC", "XYZ") == ""

def test_identical_strings():
    # Identical strings
    assert longest_common_subsequence("HELLO", "HELLO") == "HELLO"

def test_partial_match():
    # Partial matches
    assert longest_common_subsequence("ABCBDAB", "BDCABA") == "BCBA"

def test_case_sensitivity():
    # Case sensitivity
    assert longest_common_subsequence("Hello", "hello") == ""

def test_repeated_characters():
    # Repeated characters
    assert longest_common_subsequence("AAAAAA", "AAABBB") == "AAAA"

@pytest.mark.parametrize("str1,str2,expected", [
    ("ABCDGH", "AEDFHR", "ADH"),
    ("AGGTAB", "GXTXAYB", "GTAB"),
    ("Hello", "World", ""),
    ("", "Test", ""),
    ("Python", "Python", "Python")
])
def test_parameterized_cases(str1, str2, expected):
    assert longest_common_subsequence(str1, str2) == expected