import pytest
import logging
from src.sorting_performance import log_sorting_performance, bubble_sort, quick_sort

def test_log_sorting_performance():
    algorithms = {
        'bubble_sort': bubble_sort,
        'quick_sort': quick_sort
    }
    input_sizes = [10, 100, 1000]
    
    # Capture logging
    logging.getLogger().setLevel(logging.INFO)
    
    # Run performance logging
    results = log_sorting_performance(algorithms, input_sizes, num_runs=3)
    
    # Validate results structure
    assert results is not None
    assert isinstance(results, dict)
    
    # Check performance results for each input size
    for size in input_sizes:
        assert size in results
        
        # Check results for each algorithm
        for algo_name in algorithms.keys():
            assert algo_name in results[size]
            
            # Check metrics
            metrics = results[size][algo_name]
            assert 'avg_time' in metrics
            assert 'runs' in metrics
            
            # Validate metrics
            assert metrics['avg_time'] > 0
            assert len(metrics['runs']) == 3
            
            # Each run should be positive
            for run_time in metrics['runs']:
                assert run_time > 0

def test_sorting_correctness():
    # Test each sorting algorithm's correctness
    test_cases = [
        [5, 2, 9, 1, 5, 6],
        [1],
        [],
        [3, 3, 3, 3]
    ]
    
    for case in test_cases:
        bubble_sorted = bubble_sort(case.copy())
        quick_sorted = quick_sort(case.copy())
        
        assert bubble_sorted == sorted(case)
        assert quick_sorted == sorted(case)

def test_sorting_different_input_types():
    # Edge cases with varying integer inputs
    test_cases = [
        [0, 0, 0],
        [-1, -2, -3],
        [1000, -1000, 0]
    ]
    
    for case in test_cases:
        bubble_sorted = bubble_sort(case.copy())
        quick_sorted = quick_sort(case.copy())
        
        assert bubble_sorted == sorted(case)
        assert quick_sorted == sorted(case)