import pytest
from src.palindrome_check import is_palindrome

def test_is_palindrome():
    # Test basic palindromes
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    
    # Test case-insensitive palindromes
    assert is_palindrome("Racecar") == True
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    
    # Test non-palindromes
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    
    # Test edge cases
    assert is_palindrome("") == True  # Empty string
    assert is_palindrome(" ") == True  # Just whitespace
    
    # Test with punctuation and mixed case
    assert is_palindrome("Was it a car or a cat I saw?") == True
    assert is_palindrome("No 'x' in Nixon") == True
    
    # Test with numbers
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("12321") == True
    assert is_palindrome("123") == False