import pytest
import random
from src.sort_performance_logger import compare_sorting_algorithms

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
    # Test with small random list
    data = [random.randint(1, 1000) for _ in range(100)]
    
    results = compare_sorting_algorithms(bubble_sort, quick_sort, data)
    
    # Check structure of results
    assert 'algorithm1' in results
    assert 'algorithm2' in results
    assert 'faster_algorithm' in results
    
    # Check performance metrics
    for algo in ['algorithm1', 'algorithm2']:
        assert 'name' in results[algo]
        assert 'avg_time' in results[algo]
        assert 'min_time' in results[algo]
        assert 'max_time' in results[algo]
        assert results[algo]['avg_time'] >= 0
        assert results[algo]['min_time'] >= 0
        assert results[algo]['max_time'] >= 0

def test_compare_sorting_algorithms_empty_list():
    with pytest.raises(ValueError, match="Input data cannot be empty"):
        compare_sorting_algorithms(bubble_sort, quick_sort, [])

def test_compare_sorting_algorithms_sorted_list():
    data = list(range(100))
    
    results = compare_sorting_algorithms(bubble_sort, quick_sort, data)
    
    # Verify results are meaningful
    assert 'faster_algorithm' in results
    assert results['faster_algorithm'] in [bubble_sort.__name__, quick_sort.__name__]

def test_compare_sorting_algorithms_reverse_sorted_list():
    data = list(reversed(range(100)))
    
    results = compare_sorting_algorithms(bubble_sort, quick_sort, data)
    
    # Verify results are meaningful
    assert 'faster_algorithm' in results
    assert results['faster_algorithm'] in [bubble_sort.__name__, quick_sort.__name__]