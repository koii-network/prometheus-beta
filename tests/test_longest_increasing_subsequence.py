import pytest
from src.longest_increasing_subsequence import longest_increasing_subsequence

def test_longest_increasing_subsequence():
    # Test cases
    assert longest_increasing_subsequence([]) == 0, "Empty array should return 0"
    assert longest_increasing_subsequence([1]) == 1, "Single element array should return 1"
    assert longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]) == 4, "Complex case with multiple increasing subsequences"
    assert longest_increasing_subsequence([0, 1, 0, 3, 2, 3]) == 4, "Another complex case"
    assert longest_increasing_subsequence([7, 7, 7, 7, 7, 7, 7]) == 1, "All equal elements"
    
    # Edge cases
    assert longest_increasing_subsequence([-1, -2, -3]) == 1, "Decreasing negative numbers"
    assert longest_increasing_subsequence([3, 2, 1]) == 1, "Strictly decreasing array"
    
    # Large increasing subsequence
    large_sequence = list(range(1, 1001))
    assert longest_increasing_subsequence(large_sequence) == 1000, "Full increasing sequence"