import pytest
from src.palindrome_checker import is_palindrome

def test_simple_palindromes():
    """Test basic palindrome scenarios."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("") == True

def test_palindrome_with_spaces_and_punctuation():
    """Test palindromes with spaces and punctuation."""
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("race a car") == False

def test_case_insensitive():
    """Test that palindrome check is case-insensitive."""
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("RaceCar") == True

def test_non_palindromes():
    """Test non-palindrome strings."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_single_character():
    """Test single character strings."""
    assert is_palindrome("a") == True
    assert is_palindrome("b") == True

def test_invalid_input():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        is_palindrome(123)
    with pytest.raises(TypeError):
        is_palindrome(None)
    with pytest.raises(TypeError):
        is_palindrome(["not", "a", "string"])