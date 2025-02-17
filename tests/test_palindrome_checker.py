import pytest
from src.palindrome_checker import is_palindrome

def test_palindrome_basic():
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False

def test_palindrome_case_insensitive():
    assert is_palindrome("Racecar") == True
    assert is_palindrome("A man, a plan, a canal: Panama") == True

def test_palindrome_with_spaces_and_punctuation():
    assert is_palindrome("race a car") == False
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_palindrome_edge_cases():
    assert is_palindrome("") == True  # Empty string is considered a palindrome
    assert is_palindrome(" ") == True  # Whitespace-only string
    assert is_palindrome("!@#$%^") == True  # Non-alphanumeric characters

def test_palindrome_non_string_input():
    with pytest.raises(AttributeError):
        is_palindrome(12321)  # Non-string input should raise an error
    with pytest.raises(TypeError):
        is_palindrome(None)  # None input should raise an error