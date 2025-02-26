import pytest
from src.min_sum_steps import min_steps_to_target_sum

def test_basic_scenarios():
    # Basic positive scenario
    assert min_steps_to_target_sum([1, 2, 3], 6) == 2  # e.g., 1+2+3 or 2+4
    
    # Target sum is zero
    assert min_steps_to_target_sum([1, 2, 3], 0) == 0
    
    # Impossible scenario
    assert min_steps_to_target_sum([1, 2], 10) == -1

def test_complex_scenarios():
    # Mixed positive and negative numbers
    assert min_steps_to_target_sum([-1, 5, 3, -2], 4) != -1
    
    # Large range of numbers
    large_nums = [10, 20, 30, 40, 50]
    assert min_steps_to_target_sum(large_nums, 100) != -1

def test_edge_cases():
    # Empty list
    assert min_steps_to_target_sum([], 5) == -1
    
    # Single number matches target
    assert min_steps_to_target_sum([5], 5) == 1
    assert min_steps_to_target_sum([5], 6) == -1

def test_negative_scenarios():
    # Target sum with negative numbers
    assert min_steps_to_target_sum([-1, -2, -3], -6) != -1
    
    # Negative and positive mix
    result = min_steps_to_target_sum([-5, 2, 3, 1], 0)
    assert result != -1  # There should be a way to reach zero