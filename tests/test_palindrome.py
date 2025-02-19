import pytest
from src.palindrome import longest_palindromic_substring

def test_basic_palindrome():
    assert longest_palindromic_substring("babad") in ["bab", "aba"]
    assert longest_palindromic_substring("cbbd") == "bb"

def test_single_character():
    assert longest_palindromic_substring("a") == "a"
    assert longest_palindromic_substring("x") == "x"

def test_entire_string_palindrome():
    assert longest_palindromic_substring("racecar") == "racecar"
    assert longest_palindromic_substring("madam") == "madam"

def test_multiple_equal_length_palindromes():
    assert longest_palindromic_substring("baab") == "baab"

def test_no_palindrome_longer_than_one_character():
    assert len(longest_palindromic_substring("abcde")) == 1

def test_invalid_input_types():
    with pytest.raises(TypeError):
        longest_palindromic_substring(123)
    
    with pytest.raises(TypeError):
        longest_palindromic_substring(None)

def test_empty_string():
    with pytest.raises(ValueError):
        longest_palindromic_substring("")

def test_complex_palindromes():
    assert longest_palindromic_substring("forgeeksskeegfor") == "geeksskeeg"
    assert longest_palindromic_substring("aacabdkacaa") == "aca"