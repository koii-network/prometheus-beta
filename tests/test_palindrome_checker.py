import pytest
from src.palindrome_checker import is_palindrome

def test_simple_palindrome():
    """Test basic palindrome scenarios"""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True

def test_case_insensitive_palindrome():
    """Test palindromes with mixed case"""
    assert is_palindrome("Racecar") == True
    assert is_palindrome("Level") == True

def test_palindrome_with_spaces_and_punctuation():
    """Test palindromes with non-alphanumeric characters"""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_non_palindrome():
    """Test non-palindrome strings"""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_edge_cases():
    """Test various edge cases"""
    assert is_palindrome("") == True  # Empty string
    assert is_palindrome(" ") == True  # Just a space
    assert is_palindrome("a") == True  # Single character

def test_invalid_input():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        is_palindrome(123)
    with pytest.raises(TypeError):
        is_palindrome(None)
    with pytest.raises(TypeError):
        is_palindrome(["not", "a", "string"])