import pytest
from src.palindrome_checker import is_palindrome

def test_is_palindrome():
    # Test basic palindromes
    assert is_palindrome("racecar") == True
    assert is_palindrome("RaceCar") == True
    
    # Test palindromes with spaces
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("race a car") == False
    
    # Test palindromes with numbers
    assert is_palindrome("123321") == True
    assert is_palindrome("12321") == True
    
    # Test mixed case and spaces
    assert is_palindrome("Was it a car or a cat I saw?") == True
    
    # Test non-palindromes
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    
    # Test edge cases
    assert is_palindrome("") == True  # Empty string
    assert is_palindrome(" ") == True  # Only spaces
    assert is_palindrome("a") == True  # Single character
    
    # Test with special characters
    assert is_palindrome("A man, a plan, a canal: Panama!") == True