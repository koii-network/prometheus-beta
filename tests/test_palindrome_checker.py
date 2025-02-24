import pytest
from src.palindrome_checker import is_palindrome

def test_simple_palindrome():
    """Test basic palindrome cases."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("A") == True

def test_non_palindrome():
    """Test non-palindrome cases."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_palindrome_with_spaces_and_punctuation():
    """Test palindromes with spaces and punctuation."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_case_insensitive():
    """Test case-insensitive palindrome detection."""
    assert is_palindrome("Racecar") == True
    assert is_palindrome("Level") == True

def test_empty_string():
    """Test empty string case."""
    assert is_palindrome("") == True

def test_non_string_input():
    """Test non-string input raises TypeError."""
    with pytest.raises(TypeError):
        is_palindrome(12321)
    
    with pytest.raises(TypeError):
        is_palindrome(None)

def test_only_non_alphanumeric():
    """Test string with only non-alphanumeric characters."""
    assert is_palindrome("!@#") == True