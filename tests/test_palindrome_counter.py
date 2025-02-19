import pytest
from src.palindrome_counter import count_palindromic_substrings

def test_count_palindromic_substrings():
    # Test regular strings
    assert count_palindromic_substrings("abc") == 3
    assert count_palindromic_substrings("aaa") == 6
    
    # Test strings with spaces and punctuation
    assert count_palindromic_substrings("A man, a plan, a canal: Panama") == 12
    assert count_palindromic_substrings("race a car") == 3
    
    # Test empty string
    assert count_palindromic_substrings("") == 0
    
    # Test single character
    assert count_palindromic_substrings("x") == 1
    
    # Test complex string
    assert count_palindromic_substrings("hello world") == 6
    
    # Test case-insensitive
    assert count_palindromic_substrings("ABba") == 4

def test_edge_cases():
    # Test special characters
    assert count_palindromic_substrings("!@#$%^&*()") == 0
    
    # Test long string
    long_str = "a" * 100
    assert count_palindromic_substrings(long_str) == (100 * 101) // 2