import pytest
from src.palindrome_counter import count_palindromic_substrings

def test_basic_palindromes():
    assert count_palindromic_substrings("abc") == 3
    assert count_palindromic_substrings("aaa") == 6
    assert count_palindromic_substrings("racecar") == 10

def test_empty_string():
    assert count_palindromic_substrings("") == 0

def test_single_character():
    assert count_palindromic_substrings("x") == 1

def test_with_spaces_and_punctuation():
    assert count_palindromic_substrings("A man, a plan, a canal: Panama") == 13

def test_case_insensitive():
    assert count_palindromic_substrings("Abba") == 4

def test_longer_palindromes():
    assert count_palindromic_substrings("abaxyzzyxf") > 10  # Has multiple palindromic substrings