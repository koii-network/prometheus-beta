import pytest
from src.longest_palindromic_substring import find_longest_palindromic_substring

def test_basic_palindromes():
    assert find_longest_palindromic_substring("babad") in ["bab", "aba"]
    assert find_longest_palindromic_substring("cbbd") == "bb"

def test_single_char():
    assert find_longest_palindromic_substring("a") == "a"

def test_entire_string_palindrome():
    assert find_longest_palindromic_substring("racecar") == "racecar"

def test_multiple_palindromes():
    assert find_longest_palindromic_substring("forgeeksskeegfor") == "geeksskeeg"

def test_no_palindrome_longer_than_one_char():
    assert find_longest_palindromic_substring("abcdef") in list("abcdef")

def test_even_length_palindrome():
    assert find_longest_palindromic_substring("abba") == "abba"

def test_error_handling():
    with pytest.raises(TypeError):
        find_longest_palindromic_substring(12345)
    
    with pytest.raises(ValueError):
        find_longest_palindromic_substring("")