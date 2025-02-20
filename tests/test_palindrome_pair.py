import pytest
from src.palindrome_pair import palindrome_pair

def test_palindrome_pair():
    # Test cases with palindrome differences
    assert palindrome_pair([1, 2, 3, 4, 5]) == True  # Difference of 1 or 11
    assert palindrome_pair([10, 20, 30, 40, 50]) == True  # Difference of 10
    
    # Test cases without palindrome differences
    assert palindrome_pair([1, 3, 5, 7, 9]) == False
    assert palindrome_pair([2, 4, 6, 8, 10]) == False
    
    # Edge cases
    assert palindrome_pair([]) == False  # Empty list
    assert palindrome_pair([5]) == False  # Single element
    
    # More comprehensive palindrome difference scenarios
    assert palindrome_pair([1, 12, 22, 33]) == True  # 11 difference
    assert palindrome_pair([5, 15, 25, 35]) == True  # 10 difference
    assert palindrome_pair([7, 17, 27, 37]) == True  # 10 difference