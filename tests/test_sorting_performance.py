import pytest
import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from sorting_performance import compare_sorting_algorithms

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

def test_compare_sorting_algorithms():
    # Test function with two sorting algorithms
    results = compare_sorting_algorithms(bubble_sort, quick_sort)
    
    # Check that results are generated for each input size
    assert len(results) > 0
    
    # Validate each result dictionary
    for result in results:
        assert 'input_size' in result
        assert 'algorithm1_time' in result
        assert 'algorithm2_time' in result
        assert 'faster_algorithm' in result
        
        # Ensure times are positive
        assert result['algorithm1_time'] >= 0
        assert result['algorithm2_time'] >= 0
        
        # Verify faster_algorithm is correctly set
        assert result['faster_algorithm'] in ['algorithm1', 'algorithm2']

def test_performance_result_types():
    results = compare_sorting_algorithms(bubble_sort, quick_sort)
    
    for result in results:
        assert isinstance(result['input_size'], int)
        assert isinstance(result['algorithm1_time'], float)
        assert isinstance(result['algorithm2_time'], float)
        assert isinstance(result['faster_algorithm'], str)

def test_different_input_sizes():
    custom_sizes = [50, 500, 5000]
    results = compare_sorting_algorithms(bubble_sort, quick_sort, custom_sizes)
    
    # Check that results match the custom input sizes
    input_sizes = [result['input_size'] for result in results]
    assert input_sizes == custom_sizes