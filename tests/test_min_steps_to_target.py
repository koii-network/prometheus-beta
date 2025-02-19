import pytest
from src.min_steps_to_target import min_steps_to_target_sum

def test_min_steps_to_target_sum_basic():
    # Basic scenario with exact sum possible
    assert min_steps_to_target_sum([1, 2, 3, 4], 7) == 2
    
def test_min_steps_to_target_sum_subtract():
    # Scenario involving subtraction
    assert min_steps_to_target_sum([5, 3, 2, 1], 1) == 2
    
def test_min_steps_to_target_sum_mixed():
    # Mixed addition and subtraction
    assert min_steps_to_target_sum([2, 3, 5, 8], 7) == 2
    
def test_min_steps_impossible():
    # Impossible to reach target
    assert min_steps_to_target_sum([10, 20, 30], 1) == -1
    
def test_min_steps_single_element():
    # Target possible with single element
    assert min_steps_to_target_sum([5, 3, 2], 5) == 1
    
def test_min_steps_zero_target():
    # Reaching zero target
    assert min_steps_to_target_sum([1, 2, 3, -1, -2, -3], 0) in [1, 2]

def test_min_steps_negative_numbers():
    # With negative numbers
    assert min_steps_to_target_sum([-1, 1, 2, 3], 2) == 2

def test_min_steps_large_numbers():
    # With large numbers
    assert min_steps_to_target_sum([100, 200, 300, 50], 350) == 2

def test_empty_list():
    # Empty list
    assert min_steps_to_target_sum([], 5) == -1