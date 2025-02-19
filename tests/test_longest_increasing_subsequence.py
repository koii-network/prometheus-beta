import pytest
from src.longest_increasing_subsequence import find_lis_length

def test_lis_standard_cases():
    # Various standard test cases
    assert find_lis_length([10, 22, 9, 33, 21, 50, 41, 60, 80]) == 6
    assert find_lis_length([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 6

def test_lis_edge_cases():
    # Edge cases
    assert find_lis_length([]) == 0  # Empty array
    assert find_lis_length([5]) == 1  # Single element
    assert find_lis_length([5, 5, 5, 5]) == 1  # Repeated elements
    assert find_lis_length([5, 4, 3, 2, 1]) == 1  # Decreasing sequence

def test_lis_special_scenarios():
    # Special scenarios
    assert find_lis_length([1, 2, 3, 4, 5]) == 5  # Strictly increasing
    assert find_lis_length([1, 1, 2, 2, 3, 3]) == 3  # Some duplicates
    assert find_lis_length([3, 1, 4, 1, 5, 9, 2, 6, 5]) == 4  # Mixed sequence