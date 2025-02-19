import pytest
from src.palindrome_substring_finder import find_palindrome_substrings

def test_find_palindrome_substrings_normal_case():
    result = find_palindrome_substrings("aabbaa")
    assert result == ['aabbaa', 'abba', 'aa', 'bb']

def test_find_palindrome_substrings_no_palindromes():
    result = find_palindrome_substrings("abcdef")
    assert result == []

def test_find_palindrome_substrings_multiple_palindromes():
    result = find_palindrome_substrings("racecar hello")
    assert result == ['racecar', 'ello', 'll', 'ee']

def test_find_palindrome_substrings_single_character():
    result = find_palindrome_substrings("a")
    assert result == []

def test_find_palindrome_substrings_empty_string():
    result = find_palindrome_substrings("")
    assert result == []

def test_find_palindrome_substrings_invalid_input():
    with pytest.raises(TypeError):
        find_palindrome_substrings(123)

def test_find_palindrome_substrings_sorting():
    result = find_palindrome_substrings("abbaxyzzyx")
    assert result == ['xyzzyx', 'abba', 'xx', 'zz', 'bb', 'aa']