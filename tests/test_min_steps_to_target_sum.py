import pytest
from src.min_steps_to_target_sum import min_steps_to_target_sum

def test_basic_scenario():
    """Test a basic scenario with a simple solution."""
    assert min_steps_to_target_sum([1, 2, 3], 4) == 2

def test_multiple_solutions():
    """Test a scenario with multiple possible solutions."""
    assert min_steps_to_target_sum([1, 2, 3, 4], 5) == 2

def test_no_solution():
    """Test a scenario where no solution exists."""
    assert min_steps_to_target_sum([10, 20], 1) is None

def test_empty_list():
    """Test behavior with an empty list."""
    assert min_steps_to_target_sum([], 5) is None

def test_single_element_exact_match():
    """Test with a single element matching the target."""
    assert min_steps_to_target_sum([5], 5) == 1

def test_single_element_no_match():
    """Test with a single element not matching the target."""
    assert min_steps_to_target_sum([3], 5) is None

def test_negative_numbers():
    """Test with negative numbers in the input list."""
    assert min_steps_to_target_sum([-1, 2, 3], 2) == 2

def test_large_numbers():
    """Test with larger numbers."""
    assert min_steps_to_target_sum([100, 50, 25], 75) == 2

def test_zero_target():
    """Test reaching a zero target sum."""
    assert min_steps_to_target_sum([1, -1, 2, -2], 0) == 2