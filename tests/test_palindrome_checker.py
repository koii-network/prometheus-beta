import pytest
from src.palindrome_checker import is_palindrome

def test_basic_palindromes():
    # Test simple palindromes
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("A") == True

def test_palindromes_with_spaces_and_punctuation():
    # Test palindromes with spaces, different cases, and punctuation
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("Race a car") == False
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_non_palindromes():
    # Test non-palindrome strings
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_empty_string():
    # Empty string is considered a palindrome
    assert is_palindrome("") == True

def test_whitespace_string():
    # String with only whitespace is considered a palindrome
    assert is_palindrome("   ") == True

def test_invalid_input():
    # Test handling of non-string inputs
    with pytest.raises(TypeError):
        is_palindrome(12345)
    with pytest.raises(TypeError):
        is_palindrome(None)
    with pytest.raises(TypeError):
        is_palindrome(["racecar"])