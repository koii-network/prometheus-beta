import pytest
from src.palindrome_checker import is_palindrome

def test_standard_palindromes():
    """Test typical palindrome scenarios"""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_edge_cases():
    """Test edge cases like empty string, single character, and mixed case"""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome("Able was I ere I saw Elba") == True

def test_numeric_palindromes():
    """Test palindromes with numbers"""
    assert is_palindrome("12321") == True
    assert is_palindrome("123 321") == True
    assert is_palindrome("12345") == False

def test_special_characters():
    """Test palindromes with various special characters"""
    assert is_palindrome("!@#$A man, a plan, a canal: Panama!@#$") == True
    assert is_palindrome("No 'x' in Nixon") == True

def test_mixed_case():
    """Test palindromes with mixed case"""
    assert is_palindrome("RaCeCaR") == True
    assert is_palindrome("Hello") == False

def test_non_string_input():
    """Test handling of invalid input types"""
    with pytest.raises(AttributeError):
        is_palindrome(12345)
    with pytest.raises(AttributeError):
        is_palindrome(None)