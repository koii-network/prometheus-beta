import pytest
from src.longest_palindrome import find_longest_palindromic_substring

def test_basic_palindromes():
    assert find_longest_palindromic_substring("babad") in ["bab", "aba"]
    assert find_longest_palindromic_substring("cbbd") == "bb"

def test_single_character():
    assert find_longest_palindromic_substring("a") == "a"
    assert find_longest_palindromic_substring("z") == "z"

def test_entire_string_palindrome():
    assert find_longest_palindromic_substring("racecar") == "racecar"
    assert find_longest_palindromic_substring("level") == "level"

def test_multiple_palindromes():
    assert find_longest_palindromic_substring("forgeeksskeegfor") == "geeksskeeg"

def test_no_palindrome_except_single_chars():
    assert len(find_longest_palindromic_substring("abc")) == 1

def test_input_validation():
    with pytest.raises(TypeError):
        find_longest_palindromic_substring(123)
    
    with pytest.raises(TypeError):
        find_longest_palindromic_substring(None)
    
    with pytest.raises(ValueError):
        find_longest_palindromic_substring("")

def test_even_and_odd_length_palindromes():
    assert find_longest_palindromic_substring("abcba") == "abcba"
    assert find_longest_palindromic_substring("abccba") == "abccba"