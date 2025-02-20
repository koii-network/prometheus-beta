import pytest
from src.palindrome_utils import find_palindromic_substrings

def test_find_palindromic_substrings_basic():
    assert set(find_palindromic_substrings("abc")) == set(["a", "b", "c"])

def test_find_palindromic_substrings_multiple():
    assert set(find_palindromic_substrings("aaa")) == set(["a", "aa", "aaa"])

def test_find_palindromic_substrings_mixed():
    result = set(find_palindromic_substrings("racecar"))
    expected = set(["r", "a", "c", "e", "raceca", "aceca", "cec", "racecar"])
    assert result == expected

def test_find_palindromic_substrings_empty():
    assert find_palindromic_substrings("") == []

def test_find_palindromic_substrings_single_char():
    assert set(find_palindromic_substrings("x")) == set(["x"])

def test_find_palindromic_substrings_complex():
    result = set(find_palindromic_substrings("tattarrattat"))
    expected = set([
        "t", "a", "r", "tt", "ta", "at", "rat", "tat", 
        "ttat", "attat", "tattarrattat"
    ])
    assert result == expected