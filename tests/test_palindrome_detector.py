import pytest
from src.palindrome_detector import contains_palindrome

def test_contains_palindrome():
    # Test various scenarios
    assert contains_palindrome("level up") == True
    assert contains_palindrome("hello world") == False
    assert contains_palindrome("Madam, I'm Adam") == True
    assert contains_palindrome("12321 is a number") == True
    assert contains_palindrome("no palindromes here") == False
    
def test_special_characters():
    assert contains_palindrome("Hi, radar is cool!") == True
    assert contains_palindrome("a1b2c3 bob 321") == True
    
def test_case_insensitive():
    assert contains_palindrome("Madam") == True
    assert contains_palindrome("LEVEL") == True
    
def test_edge_cases():
    assert contains_palindrome("") == False
    assert contains_palindrome("a") == False
    assert contains_palindrome("!@#$%^") == False
    
def test_multiple_palindromes():
    assert contains_palindrome("level radar hello") == True