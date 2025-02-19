import pytest
from src.palindrome_checker import is_palindrome

def test_basic_palindromes():
    """Test basic palindrome strings."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("madam") == True
    assert is_palindrome("level") == True

def test_non_palindromes():
    """Test non-palindrome strings."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_palindromes_with_spaces_and_punctuation():
    """Test palindromes with spaces and punctuation."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_mixed_case_palindromes():
    """Test palindromes with mixed case letters."""
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("No 'x' in Nixon") == True

def test_empty_and_single_char_strings():
    """Test empty and single character strings."""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True
    
def test_numeric_palindromes():
    """Test palindromes with numbers."""
    assert is_palindrome("12321") == True
    assert is_palindrome("123 321") == True
    assert is_palindrome("12345") == False