import pytest
from src.palindrome_rearrange import can_form_palindrome

def test_can_form_palindrome():
    # Test cases that can form palindromes
    assert can_form_palindrome("racecar") == True
    assert can_form_palindrome("aab") == True
    assert can_form_palindrome("aabb") == True
    assert can_form_palindrome("a") == True
    assert can_form_palindrome("") == True

def test_can_form_palindrome_with_spaces():
    # Test cases with spaces
    assert can_form_palindrome("race car") == True
    assert can_form_palindrome("a man a plan a canal panama") == True

def test_cannot_form_palindrome():
    # Test cases that cannot form palindromes
    assert can_form_palindrome("code") == False
    assert can_form_palindrome("abcde") == False

def test_case_insensitive():
    # Test case insensitivity
    assert can_form_palindrome("RaceCar") == True
    assert can_form_palindrome("AbBa") == True

def test_edge_cases():
    # Edge cases
    assert can_form_palindrome(" ") == True  # Single space
    assert can_form_palindrome("   ") == True  # Multiple spaces
    assert can_form_palindrome("!@#") == False  # Non-letter characters