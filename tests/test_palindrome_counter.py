import pytest
from src.palindrome_counter import count_palindromic_substrings

def test_empty_string():
    assert count_palindromic_substrings("") == 0

def test_single_character():
    assert count_palindromic_substrings("a") == 1

def test_two_characters_same():
    assert count_palindromic_substrings("aa") == 3

def test_two_characters_different():
    assert count_palindromic_substrings("ab") == 2

def test_multiple_characters():
    assert count_palindromic_substrings("abc") == 3

def test_all_same_characters():
    assert count_palindromic_substrings("aaa") == 6

def test_complex_palindromes():
    assert count_palindromic_substrings("racecar") == 10

def test_mixed_palindromes():
    assert count_palindromic_substrings("aabaa") == 9

# Edge case tests
def test_none_input():
    with pytest.raises(TypeError):
        count_palindromic_substrings(None)

def test_non_string_input():
    with pytest.raises(TypeError):
        count_palindromic_substrings(123)