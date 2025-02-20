import pytest
from src.palindrome_rearrange import can_form_palindrome, rearrange_to_palindrome

def test_can_form_palindrome():
    # Test cases that can form palindrome
    assert can_form_palindrome("racecar") == True
    assert can_form_palindrome("aab") == True
    assert can_form_palindrome("carerac") == True
    
    # Test cases that cannot form palindrome
    assert can_form_palindrome("hello") == False
    assert can_form_palindrome("abcdef") == False

def test_rearrange_to_palindrome():
    # Test palindrome rearrangement
    result1 = rearrange_to_palindrome("aab")
    assert can_form_palindrome(result1)
    assert len(result1) == 3
    assert sorted(result1) == sorted("aab")
    
    result2 = rearrange_to_palindrome("carerac")
    assert can_form_palindrome(result2)
    assert len(result2) == 7
    assert sorted(result2) == sorted("carerac")
    
    # Test edge cases
    assert rearrange_to_palindrome("hello") == ""
    assert rearrange_to_palindrome("") == ""
    
    # Test single character
    assert rearrange_to_palindrome("a") == "a"
    
    # Test multiple character scenarios
    result3 = rearrange_to_palindrome("aabbcc")
    assert len(result3) == 6
    assert can_form_palindrome(result3)
    assert sorted(result3) == sorted("aabbcc")

def test_odd_length_palindrome():
    result = rearrange_to_palindrome("aabc")
    assert len(result) == 4
    assert can_form_palindrome(result)
    assert sorted(result) == sorted("aabc")