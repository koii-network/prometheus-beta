import pytest
from src.max_consecutive_sum import max_consecutive_substring_sum

def test_max_consecutive_substring_sum():
    # Test standard cases
    assert max_consecutive_substring_sum("abcabcbb") == 6  # a(97) + b(98) + c(99) = 294
    assert max_consecutive_substring_sum("aabacbaa") == 3  # Multiple scenarios
    
    # Edge cases
    assert max_consecutive_substring_sum("") == 0  # Empty string
    assert max_consecutive_substring_sum("a") == 97  # Single character
    
    # Various scenarios
    assert max_consecutive_substring_sum("aaa") == 97  # Repeating character
    assert max_consecutive_substring_sum("abcdef") == 597  # Strictly increasing
    
    # Complex cases
    assert max_consecutive_substring_sum("abcdabcde") == 411  # Mixed scenario