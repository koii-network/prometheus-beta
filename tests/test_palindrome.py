import pytest
from src.palindrome import is_palindrome

def test_basic_palindromes():
    """Test basic palindrome scenarios."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("") == True

def test_palindromes_with_spaces_and_punctuation():
    """Test palindromes with spaces and punctuation."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("Race a car") == False
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_case_insensitivity():
    """Test that function is case-insensitive."""
    assert is_palindrome("Madam") == True
    assert is_palindrome("MaDaM") == True
    assert is_palindrome("RACECAR") == True

def test_non_palindromes():
    """Test non-palindrome scenarios."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_edge_cases():
    """Test edge cases."""
    assert is_palindrome(" ") == True
    assert is_palindrome("!!!") == True
    assert is_palindrome("a") == True
    assert is_palindrome("ab") == False

def test_numeric_palindromes():
    """Test numeric palindromes."""
    assert is_palindrome("12321") == True
    assert is_palindrome("1 2 3 2 1") == True
    assert is_palindrome("123") == False