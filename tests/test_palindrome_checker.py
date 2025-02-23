import pytest
from src.palindrome_checker import is_palindrome

def test_basic_palindromes():
    """Test basic palindrome scenarios."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("") == True

def test_non_palindromes():
    """Test non-palindrome scenarios."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_case_insensitive():
    """Test that the function is case-insensitive."""
    assert is_palindrome("Racecar") == True
    assert is_palindrome("A man a plan a canal Panama") == True

def test_with_punctuation():
    """Test palindromes with punctuation and spaces."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == True

def test_special_cases():
    """Test edge cases like single character and spaces."""
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True
    assert is_palindrome("12321") == True

def test_input_types():
    """Test exception handling for invalid input types."""
    with pytest.raises(TypeError):
        is_palindrome(None)
    with pytest.raises(TypeError):
        is_palindrome(123)