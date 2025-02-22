import pytest
from src.palindrome_checker import is_palindrome

def test_basic_palindromes():
    """Test basic palindrome cases."""
    assert is_palindrome("racecar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("A man a plan a canal Panama") == True

def test_non_palindromes():
    """Test non-palindrome cases."""
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False

def test_edge_cases():
    """Test edge cases and boundary conditions."""
    assert is_palindrome("") == True  # Empty string
    assert is_palindrome(" ") == True  # Whitespace
    assert is_palindrome("a") == True  # Single character
    
def test_case_insensitive():
    """Test case insensitivity."""
    assert is_palindrome("Able was I ere I saw Elba") == True
    
def test_punctuation_and_spaces():
    """Test handling of punctuation and spaces."""
    assert is_palindrome("race a car") == False
    assert is_palindrome("A man, a plan, a canal: Panama!") == True
    
def test_alphanumeric():
    """Test alphanumeric palindromes."""
    assert is_palindrome("123321") == True
    assert is_palindrome("A1b22b1a") == True
    assert is_palindrome("A1b22b2a") == False