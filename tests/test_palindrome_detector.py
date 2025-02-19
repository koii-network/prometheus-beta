import pytest
from src.palindrome_detector import contains_palindrome_word

def test_contains_palindrome_word():
    # Test cases with palindrome words
    assert contains_palindrome_word("racecar is a nice word") == True
    assert contains_palindrome_word("Hello level world") == True
    assert contains_palindrome_word("radar detection system") == True
    
    # Test cases without palindrome words
    assert contains_palindrome_word("Hello world") == False
    assert contains_palindrome_word("Python is awesome") == False
    
    # Test cases with mixed content
    assert contains_palindrome_word("Check out racecar123 here") == True
    assert contains_palindrome_word("Special chars: level! wow") == True
    
    # Edge cases
    assert contains_palindrome_word("") == False
    assert contains_palindrome_word("a") == False
    assert contains_palindrome_word("12321") == False  # Numbers alone don't count
    
    # Case insensitivity
    assert contains_palindrome_word("Racecar is here") == True
    assert contains_palindrome_word("LEVEL is a word") == True