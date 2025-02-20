import pytest
from src.is_palindrome import is_palindrome

def test_is_palindrome():
    # Test basic palindromes
    assert is_palindrome("racecar") == True
    assert is_palindrome("A man a plan a canal Panama") == True
    
    # Test with punctuation and mixed case
    assert is_palindrome("A man, a plan, a canal: Panama!") == True
    assert is_palindrome("race a car") == False
    
    # Test edge cases
    assert is_palindrome("") == True  # Empty string
    assert is_palindrome("a") == True  # Single character
    assert is_palindrome("ab") == False  # Two different characters
    
    # Test with numbers and special characters
    assert is_palindrome("12321") == True
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("Hello, World!") == False