import pytest
from src.palindrome_detector import contains_palindrome_word

def test_contains_palindrome_word():
    # Test cases with palindrome words
    assert contains_palindrome_word("hello level world") == True
    assert contains_palindrome_word("radar is a cool word") == True
    assert contains_palindrome_word("A man a plan a canal Panama") == True
    assert contains_palindrome_word("racecar in the parking lot") == True
    
    # Test cases without palindrome words
    assert contains_palindrome_word("hello world") == False
    assert contains_palindrome_word("python is awesome") == False
    
    # Test cases with mixed content
    assert contains_palindrome_word("hello 12345 level") == True
    assert contains_palindrome_word("special chars: level! radar?") == True
    
    # Edge cases
    assert contains_palindrome_word("") == False
    assert contains_palindrome_word("a") == True
    assert contains_palindrome_word("123 456 789") == False
    
    # Case insensitivity
    assert contains_palindrome_word("Level is a Palindrome") == True