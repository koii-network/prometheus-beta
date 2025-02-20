import pytest
from src.palindrome_checker import is_palindrome

def test_simple_palindromes():
    # Basic palindromes with letters
    assert is_palindrome("radar") == True
    assert is_palindrome("level") == True
    assert is_palindrome("racecar") == True

def test_palindromes_with_spaces_and_punctuation():
    # Palindromes with spaces and punctuation
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome("Race a car") == False
    assert is_palindrome("Was it a car or a cat I saw?") == True

def test_mixed_case_palindromes():
    # Case-insensitive palindromes
    assert is_palindrome("Able was I ere I saw Elba") == True
    assert is_palindrome("No Lemon, No Melon") == True

def test_numeric_palindromes():
    # Numeric palindromes
    assert is_palindrome("12321") == True
    assert is_palindrome("123 321") == True
    assert is_palindrome("12345") == False

def test_empty_and_single_char():
    # Empty string and single character
    assert is_palindrome("") == True
    assert is_palindrome("a") == True
    assert is_palindrome(" ") == True

def test_non_palindromes():
    # Non-palindrome strings
    assert is_palindrome("hello") == False
    assert is_palindrome("python") == False
    assert is_palindrome("OpenAI") == False

def test_complex_strings():
    # Complex strings with symbols and mixed content
    assert is_palindrome("!@#$A man, a plan, a canal: Panama!@#$") == True
    assert is_palindrome("123-454-321") == True
    assert is_palindrome("Not a palindrome!") == False