import pytest
import random
import time
from src.sort_performance_comparison import compare_sorting_algorithms

# Sample sorting algorithms for testing
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def test_compare_sorting_algorithms_basic():
    """Test basic functionality of performance comparison"""
    result = compare_sorting_algorithms(bubble_sort, quick_sort)
    
    # Check structure of result
    assert 'algorithm1_name' in result
    assert 'algorithm2_name' in result
    assert 'performance_comparison' in result
    
    # Check performance comparison entries
    for perf_entry in result['performance_comparison']:
        assert 'input_size' in perf_entry
        assert 'faster_algorithm' in perf_entry

def test_compare_sorting_algorithms_types():
    """Verify types and properties of the comparison results"""
    result = compare_sorting_algorithms(bubble_sort, quick_sort)
    
    # Verify algorithm names are correct
    assert result['algorithm1_name'] == 'bubble_sort'
    assert result['algorithm2_name'] == 'quick_sort'
    
    # Check performance comparison details
    for perf_entry in result['performance_comparison']:
        assert isinstance(perf_entry['input_size'], int)
        assert perf_entry['input_size'] > 0
        
        # Check time measurements
        bubble_time_key = f'{bubble_sort.__name__}_avg_time'
        quick_time_key = f'{quick_sort.__name__}_avg_time'
        assert bubble_time_key in perf_entry
        assert quick_time_key in perf_entry
        
        # Time should be a positive float
        assert isinstance(perf_entry[bubble_time_key], float)
        assert isinstance(perf_entry[quick_time_key], float)
        assert perf_entry[bubble_time_key] >= 0
        assert perf_entry[quick_time_key] >= 0

def test_compare_sorting_algorithms_correctness():
    """Verify the sorting comparison handles different input sizes"""
    input_sizes = [50, 500, 5000]
    result = compare_sorting_algorithms(bubble_sort, quick_sort, input_sizes, num_runs=3)
    
    # Verify number of performance comparisons matches input sizes
    assert len(result['performance_comparison']) == len(input_sizes)
    
    # Verify each entry has correct input size
    for i, perf_entry in enumerate(result['performance_comparison']):
        assert perf_entry['input_size'] == input_sizes[i]