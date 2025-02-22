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
    assert is_palindrome("a") == True  # Single character
    
    # Test non-palindromes
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    
    # Test with numbers and mixed cases
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("A1b2c3b1a") == False