import pytest
from src.palindrome import is_palindrome

def test_is_palindrome():
    # Test basic palindromes
    assert is_palindrome("racecar") == True
    assert is_palindrome("RaceCar") == True
    
    # Test palindromes with spaces and punctuation
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    
    # Test edge cases
    assert is_palindrome("") == True  # Empty string
    assert is_palindrome(" ") == True  # Only whitespace
    assert is_palindrome("!@#$%^") == True  # Only punctuation
    
    # Test non-palindromes
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    
    # Test with numbers
    assert is_palindrome("12321") == True
    assert is_palindrome("123 321") == True
    assert is_palindrome("12345") == False