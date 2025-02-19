import pytest
from src.sorting import sort_nums, optimal_sort

def test_sort_nums_bug():
    """
    Test the bugged sorting function to demonstrate its limitations.
    """
    # Test case that will expose the bug
    test_cases = [
        [3, 1, 4, 1, 5, 9, 2, 6],  # Unsorted list with duplicates
        [9, 8, 7, 6, 5, 4, 3, 2, 1],  # Reverse sorted list
        []  # Empty list
    ]
    
    for case in test_cases:
        # The buggy sort_nums might not fully sort the list
        result = sort_nums(case.copy())
        assert result != optimal_sort(case), "Buggy sort should not work correctly"

def test_optimal_sort():
    """
    Comprehensive tests for the optimal sorting function.
    """
    test_cases = [
        # Empty list
        [],
        # Single element
        [42],
        # Already sorted list
        [1, 2, 3, 4, 5],
        # Reverse sorted list
        [5, 4, 3, 2, 1],
        # List with duplicates
        [3, 1, 4, 1, 5, 9, 2, 6],
        # Large range of numbers
        [100, -50, 0, 75, -25, 42, 12]
    ]
    
    for case in test_cases:
        # Check that optimal_sort works correctly for various inputs
        assert optimal_sort(case.copy()) == sorted(case), f"Failed to sort {case}"

def test_performance_hint():
    """
    Provide a hint about the performance difference.
    """
    # Create a large list to hint at performance differences
    large_list = list(range(10000, 0, -1))
    
    # Measure performance difference
    import timeit
    
    def time_sort_nums():
        sort_nums(large_list.copy())
    
    def time_optimal_sort():
        optimal_sort(large_list.copy())
    
    sort_nums_time = timeit.timeit(time_sort_nums, number=100)
    optimal_sort_time = timeit.timeit(time_optimal_sort, number=100)
    
    # While we don't assert exact performance, we expect optimal_sort to be significantly faster
    assert optimal_sort_time < sort_nums_time, "Optimal sort should be more efficient"