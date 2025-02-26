import pytest
from src.longest_increasing_subsequence import longest_increasing_subsequence

# (Previous tests remain the same)

def test_negative_and_mixed_integers():
    """Test sequence with negative and mixed integers"""
    arr = [-5, 3, -2, 6, 1, 7, 4, 8]
    assert longest_increasing_subsequence(arr) == 5
    assert longest_increasing_subsequence(arr, return_sequence=True) == [-5, -2, 1, 4, 8]

    arr_negative = [-10, -5, -3, -1]
    assert longest_increasing_subsequence(arr_negative) == 4
    assert longest_increasing_subsequence(arr_negative, return_sequence=True) == [-10, -5, -3, -1]