import pytest
from src.palindrome_checker import is_palindrome

def test_basic_palindromes():
    """Test basic palindrome scenarios."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome("Able was I ere I saw Elba") == True

def test_non_palindromes():
    """Test strings that are not palindromes."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_palindrome_with_punctuation():
    """Test palindromes with punctuation and mixed case."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_numeric_palindromes():
    """Test numeric palindromes."""
    assert is_palindrome("12321") == True
    assert is_palindrome("123") == False

def test_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        is_palindrome(12321)
    
    with pytest.raises(TypeError):
        is_palindrome(None)

def test_whitespace_handling():
    """Test palindromes with whitespace."""
    assert is_palindrome("  level  ") == True
    assert is_palindrome("  not  a  palindrome  ") == False