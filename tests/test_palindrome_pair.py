import pytest
from src.palindrome_pair import palindrome_pair

def test_palindrome_pair():
    # Test cases with palindrome differences
    assert palindrome_pair([1, 2, 3, 4, 5]) == True  # 2-3 = 1 (palindrome)
    assert palindrome_pair([10, 20, 30, 40]) == True  # 30-20 = 10 (palindrome)
    
    # Test cases without palindrome differences
    assert palindrome_pair([1, 3, 5, 7]) == False
    assert palindrome_pair([11, 22, 33, 44]) == False
    
    # Edge cases
    assert palindrome_pair([]) == False  # Empty list
    assert palindrome_pair([1]) == False  # Single element
    
    # Test with different palindrome differences
    assert palindrome_pair([5, 10, 15, 20, 25]) == True  # 20-15 = 5 (palindrome)
    assert palindrome_pair([100, 200, 300]) == True  # 300-200 = 100 (palindrome)

def test_palindrome_exact_matches():
    # Test cases with exact palindrome numbers
    assert palindrome_pair([11, 22, 33]) == True  # 22-11 = 11 (palindrome)
    assert palindrome_pair([101, 202, 303]) == True  # 202-101 = 101 (palindrome)

def test_negative_numbers():
    # Test with negative numbers
    assert palindrome_pair([-5, -2, 0, 3, 6]) == True  # 3-(-2) = 5 (palindrome)
    assert palindrome_pair([-10, -5, 0, 5, 10]) == True  # 5-(-5) = 10 (palindrome)