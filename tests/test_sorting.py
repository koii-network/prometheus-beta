import pytest
from src.sorting import sort_nums, optimal_sort

def test_sort_nums_bug():
    """Test the intentional bug in sort_nums function"""
    # Test that sort_nums returns only half the list
    input_list = [5, 2, 8, 12, 1, 6]
    result = sort_nums(input_list)
    
    # Check that the result is shorter than the original list
    assert len(result) == len(input_list) // 2
    
    # Verify that it doesn't fully sort the list
    assert result != sorted(input_list)

def test_optimal_sort_correctness():
    """Test the optimal sorting function"""
    # Test with various input scenarios
    test_cases = [
        [5, 2, 8, 12, 1, 6],  # Mixed positive numbers
        [-1, -5, 0, 3, -10],  # Mixed with negative numbers
        [1, 1, 1, 1],  # Repeated numbers
        [],  # Empty list
        [100]  # Single element list
    ]
    
    for case in test_cases:
        # Verify that optimal_sort matches Python's built-in sorted function
        assert optimal_sort(case) == sorted(case)

def test_sort_nums_against_optimal_sort():
    """Compare sort_nums with optimal_sort to highlight the bug"""
    input_list = [5, 2, 8, 12, 1, 6]
    
    # Sort with the buggy function
    buggy_result = sort_nums(input_list)
    
    # Sort with the optimal function
    optimal_result = optimal_sort(input_list)
    
    # Demonstrate the difference
    assert buggy_result != optimal_result
    assert len(buggy_result) != len(optimal_result)