import pytest
from src.palindrome_checker import is_palindrome

def test_basic_palindromes():
    """Test basic palindromes."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("A man a plan a canal Panama") == True
    assert is_palindrome("race a car") == False

def test_case_insensitive():
    """Test that palindrome check is case-insensitive."""
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("RaceCar") == True

def test_punctuation_and_spaces():
    """Test palindromes with punctuation and spaces."""
    assert is_palindrome("A man, a plan, a canal: Panama!") == True
    assert is_palindrome("hello world") == False

def test_empty_and_single_char():
    """Test empty string and single character."""
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True

def test_error_handling():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        is_palindrome(123)
    with pytest.raises(TypeError):
        is_palindrome(None)
    with pytest.raises(TypeError):
        is_palindrome(["not", "a", "string"])

def test_unicode_palindromes():
    """Test palindromes with unicode characters."""
    assert is_palindrome("Madam, I'm Adam") == True
    assert is_palindrome("νωων") == True  # Greek palindrome