import pytest
from src.palindrome_pair import palindrome_pair

def test_palindrome_pair_basic_cases():
    # Basic cases with palindrome differences
    assert palindrome_pair([1, 2, 3, 4, 5]) == True  # 3-1 = 2 (palindrome diff)
    assert palindrome_pair([10, 20, 30, 40]) == True  # 20-10 = 10 (palindrome diff)
    
def test_palindrome_pair_no_palindrome():
    # Cases with no palindrome differences
    assert palindrome_pair([1, 3, 5, 7]) == False
    assert palindrome_pair([2, 4, 6, 8]) == False
    
def test_palindrome_pair_edge_cases():
    # Edge cases
    assert palindrome_pair([]) == False  # Empty list
    assert palindrome_pair([1]) == False  # Single element
    assert palindrome_pair([11, 22, 33]) == True  # 22-11 = 11 (palindrome diff)
    
def test_palindrome_pair_negative_numbers():
    # Test with negative numbers
    assert palindrome_pair([-5, -3, 0, 3, 5]) == True  # 3 - (-3) = 6 (palindrome diff)
    
def test_palindrome_pair_large_numbers():
    # Test with larger numbers
    assert palindrome_pair([100, 202, 303, 404]) == True  # 202-100 = 102 (palindrome-like diff)
    assert palindrome_pair([1000, 2000, 3000]) == False