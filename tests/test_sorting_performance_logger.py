import pytest
import random
from src.sorting_performance_logger import log_sorting_performance

# Sample sorting algorithms for testing
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def python_sort(arr):
    return sorted(arr)

def test_log_sorting_performance_basic():
    # Define algorithms to test
    algorithms = {
        'bubble_sort': bubble_sort,
        'python_sort': python_sort
    }
    
    # Test with default parameters
    results = log_sorting_performance(algorithms)
    
    # Assertions
    assert isinstance(results, dict), "Results should be a dictionary"
    
    # Check results structure
    for size in [100, 1000, 10000]:
        assert size in results, f"Results should include input size {size}"
        
        # Check algorithm performance metrics
        for algo_name in algorithms.keys():
            algo_metrics = results[size][algo_name]
            
            # Check metric keys
            assert 'mean_time' in algo_metrics
            assert 'median_time' in algo_metrics
            assert 'min_time' in algo_metrics
            assert 'max_time' in algo_metrics
            assert 'std_dev' in algo_metrics
            
            # Check metric values are numeric and non-negative
            assert isinstance(algo_metrics['mean_time'], float)
            assert algo_metrics['mean_time'] >= 0
            
def test_log_sorting_performance_custom():
    # Custom input generator
    def small_range_generator(n):
        return [random.randint(1, 10) for _ in range(n)]
    
    # Define algorithms to test
    algorithms = {
        'bubble_sort': bubble_sort,
        'python_sort': python_sort
    }
    
    # Test with custom parameters
    results = log_sorting_performance(
        algorithms=algorithms,
        input_generator=small_range_generator,
        input_sizes=[50, 100],
        num_runs=3
    )
    
    # Assertions
    assert len(results) == 2  # Two input sizes
    
def test_invalid_inputs():
    # Test with empty algorithms dict
    with pytest.raises(TypeError):
        log_sorting_performance({})
    
    # Test with invalid input generator
    with pytest.raises(TypeError):
        log_sorting_performance(
            {'python_sort': python_sort}, 
            input_generator=lambda: "not a list"
        )