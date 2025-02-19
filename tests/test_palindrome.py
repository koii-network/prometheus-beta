import pytest
from src.palindrome import is_palindrome

def test_is_palindrome():
    # Test basic palindromes
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    
    # Test palindromes with different capitalization
    assert is_palindrome("Racecar") == True
    assert is_palindrome("A man a plan a canal Panama") == True
    
    # Test palindromes with punctuation
    assert is_palindrome("A man, a plan, a canal: Panama!") == True
    
    # Test non-palindromes
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    
    # Test edge cases
    assert is_palindrome("") == True  # Empty string is considered a palindrome
    assert is_palindrome(" ") == True  # Space-only string is a palindrome
    assert is_palindrome("a") == True  # Single character is a palindrome
    
    # Test with mixed alphanumeric characters
    assert is_palindrome("R2a2R") == True
    assert is_palindrome("R2a3R") == False