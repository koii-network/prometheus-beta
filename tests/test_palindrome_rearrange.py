import pytest
from src.palindrome_rearrange import can_form_palindrome, rearrange_to_palindrome

def test_can_form_palindrome():
    # Test cases where palindrome can be formed
    assert can_form_palindrome("aab") == True
    assert can_form_palindrome("racecar") == True
    assert can_form_palindrome("code") == False
    assert can_form_palindrome("aabbccc") == True
    assert can_form_palindrome("") == True
    
def test_rearrange_to_palindrome():
    # Test palindrome rearrangement
    result_aab = rearrange_to_palindrome("aab")
    assert result_aab in ["aba", "baa"]
    assert result_aab == result_aab[::-1]
    
    assert rearrange_to_palindrome("racecar") == "racecar"
    assert rearrange_to_palindrome("code") == ""
    
    # Test single character
    assert rearrange_to_palindrome("a") == "a"
    
    # Test multiple character counts
    result = rearrange_to_palindrome("aabbccc")
    assert result and is_palindrome(result)
    
def test_empty_string():
    # Test empty string
    assert rearrange_to_palindrome("") == ""
    
def test_complex_cases():
    # More complex test cases
    assert rearrange_to_palindrome("abcdefg") == ""  # Cannot form palindrome
    
    result = rearrange_to_palindrome("aaabbbc")
    assert result and is_palindrome(result)

def is_palindrome(word):
    """Helper function to check if a word is a palindrome"""
    return word == word[::-1]