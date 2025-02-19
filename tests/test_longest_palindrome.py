import pytest
from src.longest_palindrome import find_longest_palindromic_substring

def test_basic_palindromes():
    assert find_longest_palindromic_substring("babad") == "bab"
    assert find_longest_palindromic_substring("cbbd") == "bb"

def test_single_character():
    for char in "abcdefg":
        assert find_longest_palindromic_substring(char) == char

def test_full_string_palindrome():
    assert find_longest_palindromic_substring("racecar") == "racecar"
    assert find_longest_palindromic_substring("level") == "level"

def test_multiple_palindromes():
    assert find_longest_palindromic_substring("forgeeksskeegfor") == "geeksskeeg"

def test_edge_cases():
    assert find_longest_palindromic_substring("") == ""
    assert find_longest_palindromic_substring(" ") == " "

def test_no_palindrome():
    assert find_longest_palindromic_substring("abcdef") == "a"

def test_multiple_same_length_palindromes():
    result = find_longest_palindromic_substring("abaxyzzyxf")
    assert result in ["xyzzyx", "abba"]