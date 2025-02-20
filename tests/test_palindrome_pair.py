import pytest
from src.palindrome_pair import palindrome_pair

def test_palindrome_pair_positive_cases():
    # Test cases with palindrome differences
    assert palindrome_pair([1, 2, 3, 4, 5]) == True  # 2-1 = 1 (palindrome)
    assert palindrome_pair([10, 20, 30, 40, 50]) == True  # 22 (palindrome)
    assert palindrome_pair([11, 22, 33, 44, 55]) == True  # 11 (palindrome)

def test_palindrome_pair_negative_cases():
    # Test cases without palindrome differences
    assert palindrome_pair([1, 3, 5, 7, 9]) == False
    assert palindrome_pair([2, 4, 6, 8, 10]) == False

def test_palindrome_pair_edge_cases():
    # Edge cases
    assert palindrome_pair([]) == False  # Empty list
    assert palindrome_pair([1]) == False  # Single element
    assert palindrome_pair([11, 22, 33]) == True  # Palindrome difference
    
def test_palindrome_pair_large_numbers():
    # Test with larger numbers
    assert palindrome_pair([100, 200, 300, 400, 505]) == True  # 505-400 = 105 (palindrome)
    assert palindrome_pair([1000, 2000, 3000]) == False