import pytest
from src.palindrome import is_palindrome

def test_classic_palindromes():
    """Test classic palindrome strings."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_simple_palindromes():
    """Test simple palindrome scenarios."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("Racecar") == True

def test_edge_cases():
    """Test edge cases including empty string and single character."""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True

def test_numeric_palindromes():
    """Test palindromes with numbers."""
    assert is_palindrome("12321") == True
    assert is_palindrome("123 321") == True
    assert is_palindrome("12345") == False

def test_mixed_characters():
    """Test palindromes with mixed characters and punctuation."""
    assert is_palindrome("Was it a car or a cat I saw?") == True
    assert is_palindrome("No 'x' in Nixon") == True
    assert is_palindrome("Hello, World!") == False

def test_unicode_and_special_chars():
    """Test palindromes with unicode and special characters."""
    assert is_palindrome("Madam, I'm Adam.") == True
    assert is_palindrome("A Santa at NASA") == True