import pytest
from src.palindrome_checker import is_palindrome

def test_is_palindrome():
    # Test basic palindromes
    assert is_palindrome("racecar") == True
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    
    # Test non-palindromes
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    
    # Test edge cases
    assert is_palindrome("") == True  # Empty string
    assert is_palindrome(" ") == True  # Only whitespace
    assert is_palindrome("!@#") == True  # Only punctuation
    
    # Test case-insensitivity
    assert is_palindrome("Able was I ere I saw Elba") == True
    
    # Test with numbers
    assert is_palindrome("12321") == True
    assert is_palindrome("12345") == False
    
    # Test mixed alphanumeric palindromes
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("A1b22c1a") == False