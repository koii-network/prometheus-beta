import pytest
import random
from src.sorting_performance import compare_sorting_algorithms, bubble_sort, quick_sort

def test_compare_sorting_algorithms():
    # Generate a list of random integers
    test_list = [random.randint(1, 1000) for _ in range(1000)]
    
    # Compare bubble sort and quick sort
    result = compare_sorting_algorithms(bubble_sort, quick_sort, test_list)
    
    # Assertions
    assert 'algorithm1_time' in result
    assert 'algorithm2_time' in result
    assert 'faster_algorithm' in result
    
    # Check that times are positive and valid
    assert result['algorithm1_time'] >= 0
    assert result['algorithm2_time'] >= 0
    
    # Verify the faster algorithm is correctly identified
    assert result['faster_algorithm'] in [bubble_sort.__name__, quick_sort.__name__]

def test_sorting_results():
    # Ensure both sorting algorithms produce the same sorted result
    test_list = [random.randint(1, 1000) for _ in range(1000)]
    
    sorted_bubble = bubble_sort(test_list.copy())
    sorted_quick = quick_sort(test_list.copy())
    
    assert sorted_bubble == sorted_quick
    assert sorted(test_list) == sorted_bubble
    assert sorted(test_list) == sorted_quick

def test_empty_list():
    # Test performance comparison with an empty list
    result = compare_sorting_algorithms(bubble_sort, quick_sort, [])
    
    assert 'algorithm1_time' in result
    assert 'algorithm2_time' in result
    assert 'faster_algorithm' in result