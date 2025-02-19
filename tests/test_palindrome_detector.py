import pytest
from src.palindrome_detector import contains_palindrome_word

def test_contains_palindrome_word():
    # Test cases with palindrome words
    assert contains_palindrome_word("hello level world") == True
    assert contains_palindrome_word("racecar in the street") == True
    assert contains_palindrome_word("A man, a plan, a canal: Panama") == True
    assert contains_palindrome_word("These words: 12321 are interesting") == True
    
    # Test cases without palindrome words
    assert contains_palindrome_word("python is awesome") == False
    assert contains_palindrome_word("this has no palindromes") == False
    
    # Edge cases
    assert contains_palindrome_word("") == False
    assert contains_palindrome_word("a") == True
    assert contains_palindrome_word("1") == True
    
    # Mixed cases with special characters
    assert contains_palindrome_word("Hello! racecar world.") == True
    assert contains_palindrome_word("121 is a number") == True
    
    # Case insensitivity
    assert contains_palindrome_word("Level Up") == True