import pytest
from src.palindrome_validator import is_valid_palindrome

def test_valid_palindromes():
    # Test basic palindromes
    assert is_valid_palindrome("A man, a plan, a canal: Panama") == True
    assert is_valid_palindrome("race a car") == False
    
    # Test case insensitive palindromes
    assert is_valid_palindrome("Able was I ere I saw Elba") == True
    
    # Test with various punctuation and spaces
    assert is_valid_palindrome("No 'x' in Nixon") == True
    
def test_edge_cases():
    # Empty string
    assert is_valid_palindrome("") == True
    
    # Single character
    assert is_valid_palindrome("a") == True
    assert is_valid_palindrome("!@#$a@#$!") == True
    
    # Only non-alphanumeric characters
    assert is_valid_palindrome("!@#$%^&*()") == True
    
def test_non_palindromes():
    # Non-palindrome strings
    assert is_valid_palindrome("hello") == False
    assert is_valid_palindrome("python") == False
    
def test_numeric_palindromes():
    # Numeric palindromes
    assert is_valid_palindrome("12321") == True
    assert is_valid_palindrome("1 2 3 2 1") == True
    assert is_valid_palindrome("123") == False