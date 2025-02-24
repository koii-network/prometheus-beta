import pytest
from src.palindrome_validator import is_palindrome

def test_valid_palindromes():
    # Test classic palindromes with punctuation and mixed case
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    
def test_edge_cases():
    # Test empty string (considered a palindrome)
    assert is_palindrome("") == True
    
    # Test single character
    assert is_palindrome("a") == True
    assert is_palindrome("B") == True
    
def test_special_cases():
    # Test strings with various punctuation and spaces
    assert is_palindrome("Was it a car or a cat I saw?") == True
    assert is_palindrome("No 'x' in Nixon") == True
    
def test_non_palindromes():
    # Test clearly non-palindromic strings
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    
def test_numeric_palindromes():
    # Test numeric palindromes
    assert is_palindrome("1221") == True
    assert is_palindrome("123 321") == True
    assert is_palindrome("123") == False

def test_mixed_alphanumeric():
    # Test mixed alphanumeric palindromes
    assert is_palindrome("a1b2c33c2b1a") == True
    assert is_palindrome("a1b2c3") == False